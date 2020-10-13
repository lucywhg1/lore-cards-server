from flask import Flask

app = Flask(__name__)


@app.route("/info_cards")
def get_info_card():
    return {
        "id": 0,
        "title": "Shar",
        "subtitle": "The One Below",
        "summary": "Goddess of darkness, chaos, redemption, etc. All-around fairly cool lady/divinity.",
        "description": "Shar (pronounced: /ˈʃɑːr/ SHAHR[25][16]), the Mistress of the Night, was the goddess of darkness and the caverns of Faerûn, as well as a neutral evil greater deity. Counterpart to her twin Selûne, she presided over caverns, darkness, dungeons, forgetfulness, loss, night, secrets, and the Underdark.[citation needed] Among her array of twisted powers was the ability to see everything that lay or happened in the dark. Shar's symbol was a black disk with a deep purple border.[7] Shar was also the creator of the Shadow Weave, which was a counterpart and attack upon the Weave, controlled by Mystryl and her successors, before both of the Weaves fell into ruin during the Spellplague.[26]",
        "additionalSections": [
            {
                "heading": "History",
                "body": "According to one of the most ancient myths of the creation of the world and the heavens, after the universe and its crystal sphere were created by Lord Ao, there was naught but the primordial essence, the protoplasmic raw stuff of existence.",
            },
            {"heading": "Reconciliation", "body": "Jonny did this."},
        ],
        "category": {"id": 0, "name": "Religion"},
        "avatarUrl": "https://i2.wp.com/standsinthefire.com/wp-content/uploads/2015/03/255mysteris.jpg?fit=1600%2C628&ssl=1",
        "tags": [{"id": 0, "name": "gold"}],
    }
