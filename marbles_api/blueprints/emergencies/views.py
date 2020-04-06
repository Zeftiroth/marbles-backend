from flask import Blueprint, jsonify, request
# << Merge with the models for this to work, rename User and user to appropriate Model
from models.user import User
from models.emergency_contact import EmergencyContact
from playhouse.shortcuts import model_to_dict
from marbles_api.utils.mailgun import send_simple_message

emergencies_api_blueprint = Blueprint('emergencies_api',
                                      __name__,
                                      template_folder='templates')


# ------ API THAT CREATES NEW EMERGENCY CONTACT -------

@emergencies_api_blueprint.route('/new/<id>', methods=['POST'])
def create(id):

    user_id = request.json.get('user')
    name = request.json.get('name')
    contact_no = request.json.get('contact_no')
    email = request.json.get('email')
    relation = request.json.get('relation')

    # post_thread = request.get_json()

    new_contact = EmergencyContact(user_id=user_id,
                                   name=name, contact_no=contact_no, email=email, relation=relation)

    new_contact.save()

    return jsonify({
        'message': f'New Emergency Contact Made for {new_contact.user.name}',
        'user': new_contact.user.name,
        'name': new_contact.name,
        'contact_no': new_contact.contact_no,
        'email': new_contact.email,
        'relation': new_contact.relation
    }), 200

# ----- API TO DISPLAY ALL EMERGENCY CONTACTS ASSPCOATED WITH AN ID -----


@emergencies_api_blueprint.route('/<id>', methods=["GET"])
def show(id):
    econtacts = EmergencyContact.select().where(EmergencyContact.user_id == id)
    ec_data = []
    for econtact in econtacts:
        econtact = model_to_dict(econtact)
        del econtact['user']
        ec_data.append(econtact)
    return jsonify(ec_data), 200


@emergencies_api_blueprint.route('/panic/<id>', methods=["POST"])
def send(id):
    cUser = User.get_or_none(User.id == id).name
    eCont = EmergencyContact.get(EmergencyContact.user_id == id)

    eConName = eCont.name
    eConEmail = eCont.email
    eConRelation = eCont.relation

    send_simple_message(

        cUser=cUser, eConName=eConName, eConEmail=eConEmail, eConRelation=eConRelation
    )

    return jsonify({
        'message': f'Sent to {eConName} at {eConEmail}',
        'user': cUser,
        'name': eConName,
        'email': eConEmail,
        'relation': eConRelation
    }), 200
