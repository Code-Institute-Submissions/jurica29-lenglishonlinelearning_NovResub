""" System Module """
import os
from django.contrib import messages
from django.shortcuts import render, redirect
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

if os.path.exists("env.py"):
    import env

# Create your views here.
api_key = os.getenv("API_KEY", "")
list_id = os.getenv("LIST_ID", "")


def subscribeToNewsLetter(request):
    """function to manage subscriber"""
    if request.method == "POST":

        # getting users input from the form
        email = request.POST["email"]

        # initializing the mailchimp client with api key
        mailchimpClient = Client()
        mailchimpClient.set_config(
            {
                "api_key": api_key,
            }
        )

        userInfo = {
            "email_address": email,
            "status": "subscribed",
        }

        try:
            # adding member to mailchimp audience list
            mailchimpClient.lists.add_list_member(list_id, userInfo)
            messages.info(request, "You are successfully subscribed to my newsletter!")
        except ApiClientError as error:
            print(error.text)
            messages.warning(request, "Error, you have to use another email address!")

    return redirect("baseapp:home")
