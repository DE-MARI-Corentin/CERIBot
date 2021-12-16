# Projet NAO-Rasa
Contacter fabrice.lefevre@univ-avignon, 2020

##Installation

**Attention** : partout il faut utiliser la vraie IP de vos servers dans les fichiers de config (localhost ne fonctionne pas...)

### Serveur de dialogue
- Serveur RASA-X
- Aller dans PyDial et suivre instructions README
	* Conseil : installer un virtualenv (virtualenv PyDial, puis source PyDial/bin/activate ensuite)
- Lancer python tests/test_Server.py
	* Ficher de config dans test/configs/*KUSTOM* : régler l'IP
	* googleSR.py : paramètre "fr-FR" l27, à remplacer par "en-EN" pour tester les domaines par défaut

==============
Pour tester le serveur :
curl -i -X POST -H 'Content-Type:' http://192.168.1.57:5000/google?data:"AAD//wUA8f8kAML/TADX/8n75fqn9iH5GwbCBywEzQEMBsgNygx0ChcMNArNCDwFWf2sARMKrgwsBHn31vbW/tf+jPvs/WIDnQZa/pP1"& params:"KDEsIDIsIDE2MDAwLCA3MzcyOCwgJ05PTkUnLCAnbm90IGNvbXByZXNzZWQnKQ=="

==> doit produire une erreur car le fichier audio, data=, n'est pas complet
==============

### Serveur de reconnaissance de parole
- Serveur googleSR.py
- A installer dans un virtualenv (avec au moins "pip install speechRecognition). Et penser au 'source projet_robotparlant/bin/activate' à chaque fois !

==============
Pour tester le serveur :
curl -i -X POST -H 'Content-Type: application/json' -d '{"sender":"toto","message":"hello"}' http://10.126.8.106:5005/webhooks/rest/webhook/

==> doit produire (variable selon les modèles chargés bien sur) :
HTTP/1.1 200 OK
Connection: keep-alive
Keep-Alive: 5
Content-Length: 63
Content-Type: application/json

[{"recipient_id":"toto","text":"I am a bot, powered by Rasa."}]
==============

### NAO
- Démarrer Chorégraphe
- Ouvrir Projet NaoRasaProject/NaoRasa.pml
- Modifier boites RasaCall et SpeechRecognition pour ajuster les IP des serveurs
- Connecter au NAO (soit filaire, soit wifi)
- Charger le projet sur le robot (F5)
- Tester

Merci à N. Duret et L. Fournié, @CERI19, pour avoir fourni la base de de ce travail.

# A FAIRE
- faire la storie qui liste les catégories
- mettre les stories sous forme de checkpoint

##### Exemple
stories:
- story: beginning of flow
  steps:
  - intent: greet
  - action: action_ask_user_question
  - checkpoint: check_asked_question

- story: handle user affirm
  steps:
  - checkpoint: check_asked_question
  - intent: affirm
  - action: action_handle_affirmation
  - checkpoint: check_flow_finished

- story: handle user deny
  steps:
  - checkpoint: check_asked_question
  - intent: deny
  - action: action_handle_denial
  - checkpoint: check_flow_finished

- story: finish flow
  steps:
  - checkpoint: check_flow_finished
  - intent: goodbye
  - action: utter_goodbye