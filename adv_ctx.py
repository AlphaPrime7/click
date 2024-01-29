#check context for
# Run as so  python adv_ctx.py README.md check_context_object

#COMMAND GROUP 1-JSON
import pprint
import click
import json

@click.group("cli")
@click.pass_context
@click.argument("document")

def cli(ctx, document):
   """An example CLI for interfacing with a document"""
   _stream = open(document)
   _dict = json.load(_stream)
   _stream.close()
   ctx.obj = _dict

@cli.command("check_context_object")
@click.pass_context
def check_context(ctx):
   pprint.pprint(type(ctx.obj))

pass_dict = click.make_pass_decorator(dict)

@cli.command("get_keys")
@pass_dict
def get_keys(_dict):
   keys = list(_dict.keys())
   click.secho("The keys in our dictionary are", fg="green")
   click.echo(click.style(keys, fg="blue"))

@cli.command("get_key")
@click.argument("key")
@click.pass_context
def get_key(ctx, key):
   pprint.pprint(ctx.obj[key])

@cli.command("get_summary")
@click.pass_context
def get_summary(ctx):
   ctx.invoke(get_key, key="summary")

@cli.command("get_results")
@click.option("-d", "--download", is_flag=True, help="Pass to download the result to a json file")
@click.option("-k", "--key", help="Pass a key to specify that key from the results")
@click.pass_context
def get_results(ctx, download: bool, key: str):
   results = ctx.obj['results']
   if key is not None:
       result = {}
       for entry in results:
           if key in entry:
               if key in result:
                   result[key] += entry[key]
               else:
                   result[key] = entry[key]
       results = result
   if download:
       if key is not None:
           filename = key+'.json'
       else:
           filename = "results.json"
       with open(filename, 'w') as w:
           w.write(json.dumps(results))
       print("File saved to", filename)
   else:
       pprint.pprint(results)

@cli.command("get_text")
@click.option("-s", "--sentences", is_flag=True, help="Pass to return sentences")
@click.option("-p", "--paragraphs", is_flag=True, help="Pass to return paragraphs")
@click.option("-d", "--download", is_flag=True, help="Download as a json file")
@click.pass_obj
def get_text(_dict, sentences, paragraphs, download):
   """Returns the text as sentences, paragraphs, or one block by default"""
   results = _dict['results']
   text = {}
   for idx, entry in enumerate(results):
       if paragraphs:
           text[idx] = entry['text']
       else:
           if 'text' in text:
               text['text'] += entry['text']
           else:
               text['text'] = entry['text']
   if sentences:
       sentences = text['text'].split('.')
       for i in range(len(sentences)):
           if sentences[i] != '':
               text[i] = sentences[i]
       del text['text']
   pprint.pprint(text)
   if download:
       if paragraphs:
           filename = "paragraphs.json"
       elif sentences:
           filename = "sentences.json"
       else:
           filename = "text.json"
       with open(filename, 'w') as w:
           w.write(json.dumps(results))
       print("File saved to", filename)

#def main():
 #  cli(prog_name="cli")

#if __name__ == '__main__':
 #  main()


#COMMAND GROUP 2 -MP3
import requests
from time import sleep
from configure import auth_key
import json
import sys
 
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
headers = {
   "authorization": auth_key,
   "content-type": "application/json"
}
CHUNK_SIZE = 5242880

@click.group("assembly")
@click.pass_context
@click.argument("location")
def assembly(ctx, location):
   """A CLI for interacting with AssemblyAI"""
   def read_file(location):
       with open(location, 'rb') as _file:
           while True:
               data = _file.read(CHUNK_SIZE)
               if not data:
                   break
               yield data
          
   upload_response = requests.post(
       upload_endpoint,
       headers=headers, data=read_file(location)
   )
   audio_url = upload_response.json()['upload_url']
   print('Uploaded to', audio_url)
   transcript_request = {
       'audio_url': audio_url,
       'iab_categories': 'True',
   }
 
   transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
   transcript_id = transcript_response.json()['id']
   polling_endpoint = transcript_endpoint + "/" + transcript_id
   print("Transcribing at", polling_endpoint)
   polling_response = requests.get(polling_endpoint, headers=headers)
   while polling_response.json()['status'] != 'completed':
       sleep(30)
       print("Transcript processing ...")
       try:
           polling_response = requests.get(polling_endpoint, headers=headers)
       except:
           print("Expected to wait 30 percent of the length of your video")
           print("After wait time is up, call poll with id", transcript_id)
           return transcript_id
   categories_filename = transcript_id + '_categories.json'
   with open(categories_filename, 'w') as f:
       f.write(json.dumps(polling_response.json()['iab_categories_result']))
   print('Categories saved to', categories_filename)
   ctx.obj = polling_response.json()['id']


def main():
   if ".json" in sys.argv[1]:
       cli(prog_name="cli")
   if ".mp3" in sys.argv[1]:
       assembly(prog_name="assembly")