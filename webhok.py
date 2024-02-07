import streamlit as st
import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjUwNTY4MDYzNzA0MzI1MjY0NTUzNzUxMzci_pc"


# Function to post data to the webhook using argument unpacking
def post_to_webhook(**data):
    response = requests.post(WEBHOOK_URL, json=data)
    return response


st.title("🎬 OBTENIR VOTRE DEVIS ")

st.markdown(
    """
🚗 Commencez Votre Voyage Sans Souci Aujourd'hui!

"""
)

with st.form(key="idea_form"):
    Nom = st.text_input("Name (optional)", placeholder="Your Name")
    Ventes = st.text_input("VENTES (optional)", placeholder="Vente_journalière")
    Fiches = st.text_input("FICHES", placeholder="Nombres de Fiches ...")
    Contrats = st.text_input("contrat (optional)", placeholder="Nombres de contrat souscrit")
    CB1 = st.text_input("CB1 (optional)", placeholder="Montant CB1")
    CB2 = st.text_input("CB2 (optional)", placeholder="Montant CB2")
    Primme_mensuelle = st.text_input("Montant Prime_mensuelle (optional)", placeholder="Prime_mensuelle")
    TotalFrais = st.text_input("total frais (optional)", placeholder="Montant Frais")
    ID = st.text_input("ID (optional)", placeholder="Code_courtier")
    Email = st.text_input("email (optional)", placeholder="Email_courtier")


    submit_button = st.form_submit_button(label="Submit Idea 🚀")

    if submit_button:
        if not Fiches.strip():
            st.error("Please enter a video idea. 💡")
            st.stop()

        data = {"Nom": Nom, "Ventes": Ventes, "Fiches": Fiches, "Contrats":Contrats, "CB1":CB1,"CB2":CB2,"Primme_mensuelle":Primme_mensuelle, "TotalFrais":TotalFrais,"ID":ID,"Email":Email}
        response = post_to_webhook(**data)
        if response.status_code == 200:
            st.success("Thanks for your submission! 🌟")
        else:
            st.error("There was an error. Please try again. 🛠️")

st.markdown(
    """
        Confidentialité Assurée: Vos données sont sécurisées et traitées avec la plus grande confidentialité. Urgence Assurances s'engage à protéger vos informations.
        """)