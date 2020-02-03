# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./HaniumChatbot-b41d1dc7c0de.json"
import six
# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u'안녕 잘 지냈니? 내 이름은 정헌진이야.'
if isinstance(text, six.binary_type):
    text = text.decode('utf-8')
type = enums.Document.Type.PLAIN_TEXT
document = types.Document(
    content=text,
    type=type)

print('Text: {}'.format(text))

# 감정분석
# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment
print('=' * 20)
print(u'{:<16}: {}, {}'.format('sentiment', sentiment.score, sentiment.magnitude))
print('=' * 40)
print('=' * 40)

# 항목분석
# Detects entities in the document.
entities = client.analyze_entities(document).entities
for entity in entities:
    entity_type = enums.Entity.Type(entity.type)
    print('='*20)
    print(u'{:<16}: {}'.format('name', entity.name))
    print(u'{:<16}: {}'.format('type', entity_type.name))
    print(u'{:<16}: {}'.format('salience', entity.salience))
    print(u'{:<16}: {}'.format('wikipedia_url', entity.metadata.get('wikipedia_url', '-')))
    print(u'{:<16}: {}'.format('mid', entity.metadata.get('mid', '-')))
print('=' * 40)
print('=' * 40)

# 구문분석
# Detects syntax in document.
tokens = client.analyze_syntax(document).tokens
for token in tokens:
    part_of_speech_tag = enums.PartOfSpeech.Tag(token.part_of_speech.tag)
    print(u'{:<16}: {}'.format(part_of_speech_tag.name, token.text.content))
print('=' * 40)
print('=' * 40)

# 항목 감정분석
# 한글은 지원하지 않음.
# offset이란 해당 entity가 몇번째 음절에서 시작되는지를 의미함.
# Detects and send native python encoding to receive correct word offset.
text = u'Hi. How are you? My name is HeonJin Jeong'
if isinstance(text, six.binary_type):
    text = text.decode('utf-8')
type = enums.Document.Type.PLAIN_TEXT
document = types.Document(
    content=text,
    type=type)

encoding = enums.EncodingType.UTF32
result = client.analyze_entity_sentiment(document, encoding)
for entity in result.entities:
    print('Mentions: ')
    print(u'{:<16}: {}'.format('name', entity.name))
    for mention in entity.mentions:
        print('=' * 20)
        print(u'{:<16}: {}'.format('begin offset', mention.text.begin_offset))
        print(u'{:<16}: {}'.format('content', mention.text.content))
        print(u'{:<16}: {}'.format('magnitude', mention.sentiment.magnitude))
        print(u'{:<16}: {}'.format('sentiment', mention.sentiment.score))
        print(u'{:<16}: {}'.format('type', mention.type))
    print(u'{:<16}: {}'.format('salience', entity.salience))
    print(u'{:<16}: {}'.format('sentiment', entity.sentiment))
print('=' * 40)
print('=' * 40)

# 콘텐츠 분류
# Classify contents in document.
text = 'Android is a mobile operating system developed by Google, ' \
       'based on the Linux kernel and designed primarily for ' \
       'touchscreen mobile devices such as smartphones and tablets.'
type = enums.Document.Type.PLAIN_TEXT
if isinstance(text, six.binary_type):
    text = text.decode('utf-8')
document = types.Document(
    content = text.encode('utf-8'),
    type = type
)
categories = client.classify_text(document).categories
for category in categories:
    print('=' * 20)
    print(u'{:<16} : {}'.format('name', category.name))
    print(u'{:<16} : {}'.format('confidence', category.confidence))
