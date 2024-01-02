def get_room_number(request):
    pk = request.GET.get('id')
    print(pk)
    print("enter")
    if Room.objects.filter(room_type=pk).exists():
        room = Room.objects.get(room_type=pk,is_deleted=False
#         for passing a queryset use list() and values() to take only needed elements--- important cannot pass uuid
#        subjects = list(Subject.objects.filter(semester=sem,is_deleted=False).values('name','subject_code','semester','subject_type'))

        response_data = {
            "status" : "true",
            "room_number" : str(room.room_number),
        }
    else:
        response_data = {
            "status" : "false",
            "message" : "Room Number is not exists."
        }
    return HttpResponse(json.dumps(response_data),content_type='application/javascript')

                                
                                
                                
                                
                                
                                .
