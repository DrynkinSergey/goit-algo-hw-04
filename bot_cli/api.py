def add_contact(args, contacts):
    try:
        name, phone = args
        contacts.append({'name':name, 'phone':phone})
        return "Contact has been added!"
    except ValueError:
        return f"Args {args} is not correct... Example 'add Olena 0932223355' "
    
    
def change_contact(args, contacts):
    try:
        name, phone = args
        for index, item in enumerate(contacts):
            if item['name'] == name:
                contacts[index] = {**contacts[index], 'phone':phone}
        return "Contact has been updated!"
    except ValueError:
        return f"Args {args} is not correct... Example 'update Olena 0932223355' "


def delete_contact(args, contacts):
    name = args[0]
    for index, item in enumerate(contacts):
        if item['name'] == name:
            del contacts[index]
        else:
            print('Contact is not exists')
    return "Contact has been deleted!"


def help():
      print("Available commands: \n")
      print("- add name number")
      print("- update name number ")
      print("- delete name")
      print("- all (saw all contacts) \n")