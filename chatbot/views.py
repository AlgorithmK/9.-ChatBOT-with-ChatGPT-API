from django.shortcuts import render, redirect
import openai
from .models import Past
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        question = request.POST['question']
        
        # Set API key
        openai.api_key = "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"
        past_responses = request.POST['past_responses']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        
        #Parse the response
        response = (response["choices"][0]["text"]).strip()
        
        #Logic for psat_responses
        if '41aleks41' in past_responses:
            past_responses = response
        else:
            past_responses = f"{past_responses}<br/><br/>{response}"

        #Save to db
        record = Past(question=question, answer=response)
        record.save()
            
        return render(request, 'home.html', {"question":question, "response":response, "past_responses": past_responses})

    return render(request, 'home.html', {})


def past(request):
    past = Past.objects.all()
    return render(request, 'past.html', {"past":past})

def delete_past(request, Past_id):
    past = Past.objects.get(pk=Past_id)
    past.delete()
    messages.success(request, ("That Question and Answer where deleted"))
    return redirect('past')