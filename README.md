This repository contains a simplified replica of the Airbnb website

### Command interpreter  

Tool that allows the manipulation (creation, modification, deletion, display) of instances of any of the classes defined in the folder "models".  

This tool accepts six commands: all, create, destroy, quit, update and show, each of which will have the following syntax:  

all | all [class]  
create [class]  
destroy [class] [id]  
quit  
update [class] [id] [attribute] [value]  
show [class] [id]  

#### Examples
Let the following "__objects" attribute of a FileStorage instance:  
__objs = {
	"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521", "__class__": "BaseModel"},  
	"BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337", "__class__": "BaseModel"},  
	"BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049", "__class__": "BaseModel"},  
	"BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852", "__class__": "BaseModel"},  
	"BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287", "__class__": "BaseModel"},  
	"User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at": "2017-09-28T21:11:42.848279", "updated_at": "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", "first_name": "Betty", "__class__": "User", "last_name": "Bar", "password": "root"},  
	"User.d0ef8146-4664-4de5-8e89-096d667b728e": {"id": "d0ef8146-4664-4de5-8e89-096d667b728e", "created_at": "2017-09-28T21:11:42.848280", "updated_at": "2017-09-28T21:11:42.848294", "email": "airbnb_2@mail.com", "first_name": "John", "__class__": "User", "password": "root"}  
}

If we run ./console.py we get prompted for an input, like so:  

(hbnb)  

If we punch in the following input:

(hbnb) all User  

We will get a list of all instances of the class User that have been saved in the path of our storage. Which in this case is as follows

[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'last_name': 'Bar', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'first_name': 'Betty'}  

[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'first_name': 'John'}

We could also create an empty new instance of any class already defined in the folder "models", like so

(hbnb) create City

which will yield as output the id of the instance just created and saved, let's say it is "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4" for this example.  

That way, we can see our new instance in the storage, by writing the following  

(hbnb) show City 2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4  

which will display something along the lines of  

[City] {2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4} {'id': '{'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}
  
We could also add new attributes to our instance, or modify existing ones, like so  

(hbnb) City 2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4 Marco Polo  

which creates the attribute "Marco" with the value "Polo"

Now let's take a final look at our instance before we delete it

(hbnb) show City 2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4  

[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}

Now we can delete the instance we just created from our storage by writing the following   

(hbnb) destroy City 2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4

If we use the command "all", our short-lived City instance will no longer be available

Finally, we can exit our command interpreter by using the quit command

(hbnb) quit
