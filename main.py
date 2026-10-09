from pyscript import document,display



club_members = ('Edrian Correa', 'Dylan Alip', 'Joanna Evangelista', 'Renn Santos')

def Search(event=None):

    first_name = document.getElementById("First").value
    last_name = document.getElementById("Last").value
    combined_name = f"{first_name} {last_name}"

    member = combined_name in club_members
    messages = [f"Oops!, {combined_name} you were not accepted.", f"Congratulations!, {combined_name} you are officially apart of the ICT club."]

    display(messages[member], target="result")