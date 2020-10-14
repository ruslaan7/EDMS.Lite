from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from project.forms import DocumentForm
from project.models import User, Document
from django.core.signing import Signer
from django.core import signing


def home(request):
    return redirect(account)


@login_required(login_url='/sign_in')
def docs(request):
    user_info = request.user
    user_form = User.objects.get(id=user_info.id)
    document_form = Document.objects.filter(connection_id=user_info.id)
    return render(request, 'docs.html', {
        'user_form': user_form,
        'document_form': document_form
    })


@login_required(login_url='/sign_in')
def account(request):
    user_info = request.user
    user_form = User.objects.get(id=user_info.id)
    return render(request, 'account.html', {
        'user_form': user_form,
    })


@login_required(login_url='/sign_in')
def docsadd(request):
    form = DocumentForm()
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.connection_id = request.user.id
            document.save()
            return redirect(docs)
    return render(request, 'docsadd.html', {
        'form': form
    })


@login_required(login_url='/sign_in')
def docsedit(request, doc_id):
    document_form = DocumentForm(instance=Document.objects.get(id=doc_id))
    if request.method == "POST":
        document_form = DocumentForm(request.POST, request.FILES, instance=Document.objects.get(id=doc_id))
        if document_form.is_valid():
            document_form.save()
            return redirect(docs)
    return render(request, 'docsedit.html', {
        'document_form': document_form
    })


@login_required(login_url='/sign_in')
def docsdelete(request):
    user_info = request.user
    document_form = Document.objects.filter(connection_id=user_info.id)
    if request.method == "POST":
        document_form.filter(name=request.POST.get("doc_name"), connection_id=user_info.id).delete()
        return redirect(docs)
    return render(request, 'docsdelete.html', {
        'document_form': document_form
    })


@login_required(login_url='/sign_in')
def docssend(request):
    user_info = request.user
    user_form = User.objects.get(id=user_info.id)
    document_form = Document.objects.filter(connection_id=user_info.id)
    return render(request, 'docssend.html', {
        'user_form': user_form,
        'document_form': document_form
    })


@login_required(login_url='/sign_in')
def docssenduser(request, doc_id):
    user_info = request.user
    user_form = User.objects.exclude(username=user_info)
    if request.method == "POST":
        document = Document.objects.get(id=doc_id)
        d = User.objects.filter(username=request.POST.get("doc_name")).values('id')[0]["id"]
        a = Document.objects.filter(id=doc_id).values("document")[0]["document"]
        with open("../EDMS/media/" + a, 'r') as f:
            signer = Signer()
            txt = f.read()
            value = signer.sign(txt)
            try:
                signer.unsign(value)
                doc = Document.objects.get(pk=doc_id)
                doc.pk = None
                doc.save()
                document.connection_id = d
                document.save()
            except signing.BadSignature:
                print("Файл модифицирован!")
        return redirect(docs)
    return render(request, 'docssenduser.html', {
        'user_form': user_form
    })
