import wikipedia
print(wikipedia.summary('KamalHasan'))
wikipedia.search("Barack")
ny = wikipedia.page("Chennai")
ny.title
ny.url
ny.content
ny.links[0]
wikipedia.set_lang("fr")
wikipedia.summary("facebook", sentences=1)
wikipedia.set_lang("en")
wikipedia.summary("facebook", sentences=1)
