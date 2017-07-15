import json
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import UserInformation,ConnectionDetail
from rango.forms import UserInformationForm,ConnectionDetailForm
from django.views.decorators.csrf import csrf_exempt

def index(request):
    user_list = UserInformation.objects.all()
    context_dict = {'users' : user_list}
    return render(request, 'rango/index.html', context_dict)

@csrf_exempt
def startsession(request,sessionid):
    filedivi=[]
    folderdivi=[]
    context_dict={'id' : sessionid , 'requested_content':'' ,'interact_content':''}
    if request.method == 'POST':
        name = request.POST.get('Requested_Android')
        inter = request.POST.get('Ask_Android')
        repo = request.POST.get('Reponse_From')
        init = request.POST.get('Session_Start')
        # filedivi = request.POST.getlist('file_send')
        # folderdivi = request.POST.getlist('folder_send')
        try:
            divi = json.loads(request.body)
            filedivi = divi['file']
            folderdivi = divi['folder']
            print "filedivi is : " , filedivi
            print "folderdivi is : " , folderdivi
            #print "divi is of type" , type(divi)
        except Exception as e:
            pass
            print str(e)

        #INITIALIZATION OF SESSION BEGIN
        if init is not None:
            filename1='repo'+str(sessionid)
            filename2='inter'+str(sessionid)
            filename3=str(sessionid)
            filename4='file'+str(sessionid)
            filename5='folder'+str(sessionid)
            f1=open(filename1,"w+")
            f2=open(filename2,"w+")
            f3=open(filename3,"w+")
            f4=open(filename4,"w+")
            f5=open(filename5,"w+")
            f1.write("")
            f2.write("")
            f3.write("")
            f4.write("")
            f5.write("")
            print "INITIALIZATION done for " + str(sessionid)

        #RESPONSE CONTENT
        if repo is not None:
            filename='repo'+str(sessionid)
            fs=open(filename,'w+')
            fs.write(str(repo))
            fs.close()

        #INTERACTION CONTENT
        if inter is not None:
            filename='inter'+str(sessionid)
            fs=open(filename,'w+')
            fs.write(str(inter))
            fs.close()

        #NORMAL REQUEST
        if name is not None:
            filename=str(sessionid)
            fs=open(filename,'w+')
            fs.write(str(name))
            fs.close()

        #RETURNED FILES/FOLDER FROM CLIENT
        if filedivi or folderdivi:
            #print "filedivi is : " , filedivi
            #print "folderdivi is : " , folderdivi
            filename='file'+str(sessionid)
            fi=open(filename,'w+')
            fileString=""
            totalfile= filedivi
            for file in totalfile:
                fileString += file
                fileString += "\n"
            print "folder string is : " +  fileString
            foldername = 'folder'+str(sessionid)
            fs=open(foldername,'w+')
            folderString=""
            totalfolder = folderdivi
            for folder in totalfolder:
                folderString += folder
                folderString += "\n"
            print "folder string is :" + folderString
            fs.write(folderString)
            fi.write(fileString)


    interact=""
    requested=""
    returned=""
    files=""
    folder=""

    try:
        #normal file
        fsname=str(sessionid)
        fs=open(fsname,'r')
        for line in fs: #normal file
            requested+=str(line)
    except Exception as e:
        pass

    try:
        #interaction session file
        finame='inter'+str(sessionid)
        fi=open(finame,'r')
        for line in fi: #interaction file
            interact+=str(line)
    except Exception as e:
        pass

    try:
        #reponse from
        frname='repo'+str(sessionid)
        fr=open(frname,'r')
        for line in fr: #returned file
            print line
            returned+=str(line)
    except Exception as e:
        pass

    try:
        #reponse files
        frname='file'+str(sessionid)
        fr=open(frname,'r')
        for line in fr: #returned file
            print line
            files+=str(line).strip()
            files+="@"
    except Exception as e:
        pass

    try:
        #reponse folders
        frname='folder'+str(sessionid)
        fr=open(frname,'r')
        for line in fr: #returned file
            print line
            folder+=str(line).strip()
            folder+="@"
    except Exception as e:
        pass

    print "reuqested : " + requested
    print "interact : " + interact
    print "returned : " + returned
    print "files : " + files
    print "folders : " + folder
    context_dict['requested_content']=requested
    context_dict['interact_content']=interact
    context_dict['return_values']=returned
    context_dict['files']=files
    context_dict['folder']=folder

    return render(request,'rango/session.html',context_dict)

@csrf_exempt
def about(request):
    if request.method == 'POST':
        j = json.loads(request.body)
        print j['key']

    return HttpResponse("This is about page!!")

@csrf_exempt
def add_user(request):
    form = UserInformationForm()

    if request.method == 'POST': #method to be invoke via app or pc-client
        form = UserInformationForm(request.POST)
        pcname=""
        appname=""
        username = request.POST.get('NAME')
        uniId = request.POST.get('UNIQUEID')
        email = request.POST.get('EMAIL')
        password = request.POST.get('EMAILPASS')
        fbkey = request.POST.get('FBOATH')
        add_pc_attr = str(request.POST.get('add_pc_attr')) #ON / None
        add_android_attr = str(request.POST.get('add_android_attr')) #ON / None
        userinfo = UserInformation(name=username,uniqueid=uniId,email=email,email_password=password,fbOath=fbkey)
        if add_pc_attr == "ON":
            pcname = uniId+"@"+"PC"
        if add_android_attr == "ON":
            appname = uniId+"@"+"APP"
        connectiondetail = ConnectionDetail(pc=pcname,app=appname)
        userinfo.save()
        uni = UserInformation.objects.get(uniqueid=uniId)
        connectiondetail.uniqueid = uni
        connectiondetail.save()
        print "saved successfully"
    return render(request,'rango/add_user.html',{'form' : form})
