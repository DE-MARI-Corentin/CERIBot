from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from service import media_rss_service
from service import media_rss_url

import unidecode

lst_articles = {}
url = ""
page = 1
MediaRssService = media_rss_service.MediaRssService()


class ActionArticles(Action):
    def name(self) -> Text:
        return "action_articles"

    def identificationCategory(self, category: str) -> str:
        if category == None :
            key = media_rss_url.LE_MONDE_MAIN
        else :
            key = media_rss_url.LE_MONDE_CATEGORIES[unidecode.unidecode(category).lower()]
        return key

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global url
        global lst_articles
        global MediaRssService
        url = self.identificationCategory(str(tracker.get_slot("category")))
        lst_articles = MediaRssService.get_rss_articles(url)
        resutl = ""
        for article in lst_articles:
            resutl += "Article " + str(lst_articles.index(article)+1) + ", " + article.title + ". "

        dispatcher.utter_message(resutl)
        return []

class ActionNext(Action):
    def name(self) -> Text:
        return "action_next"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global page
        global MediaRssService
        page += 1
        lst_articles = MediaRssService.get_rss_articles(url, page * 3,page * 3 + 3)
        result = ""
        for article in lst_articles:
            result += "Article " + str(lst_articles.index(article)+1) + ", " + article.title + ". "

        dispatcher.utter_message(result)
        return []

class ActionDetails(Action):
    MediaRssService = media_rss_service.MediaRssService()
    def name(self) -> Text:
        return "action_details"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global lst_articles
        article_id = int(tracker.get_slot("details"))-1
        if len(lst_articles) > article_id > -1:
            answer = lst_articles[article_id].summary
        else :
            answer = "Aucun des articles trouvés ne correspondent à votre recherche."
        dispatcher.utter_message(answer)
        return []

class ActionCategory(Action):
    def name(self) -> Text:
        return "action_category"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        answer = "Voici la liste des catégories, "
        for category in media_rss_url.LE_MONDE_CATEGORIES:
            answer += category + ", "
        dispatcher.utter_message(answer)
        return []