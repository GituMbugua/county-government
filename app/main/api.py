from flask import Flask, request, jsonify, make_response
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from ..models import County, Constituency, Party, MCA, Governor, DeputyGovernor, Senator, WomanRep, User
from . import main
from ..import db
from collections import defaultdict


@main.route('/counties', methods=['GET'])
# @token_required
def get_counties():
    counties = County.query.all()
    output = []

    for county in counties:
        county_data = {}
        county_data["id"] = county.id
        county_data["County"] = county.name

        output.append(county_data)

    return jsonify({"Counties": output})

    return jsonify({"Status": "ok"})


# @main.route('/constituencies', methods=['GET'])
# # @token_required
# def get_constituencies():
#     constituencies = Constituency.query.all()
#     output = []
#     constituency_data = {}
#     for constituency in constituencies:
#         if constituency.county_code:
#             constituency_data['County'] = constituency.county.name
#             constituency_data['Constituency'] = constituency.name
#         output.append(constituency_data)
#     return jsonify({"Constituencies": output})
#     return jsonify({"Status": "ok"})


@main.route('/counties/constituencies', methods=['GET'])
def get_constituencies_by_id():
    constituency_data = {}
    output = []
    response = []
    # counties = County.query.all()
    # for county in counties:
    #     county_name = county.name

    # constituencies = Constituency.query.filter(
    #     county_code=x).all()
    # all_constituencies = Constituency.query.all()
    # counties = County.query.all()
    # for county in counties:
    #     print(county.constituencies.count()
    # print(counties)
    # print(len(counties))
    # for x in range(1, len(counties)):
    #     print(x)
    #     print(counties[x])
    # for x in range(0, length):
    #     print(constituencies[x])
    constituencies = Constituency.query.all()
    for constituency in constituencies:
        s = [(constituency.county.name, constituency.name)]
        # constituency_data['County'] = constituency.county.name
        if constituency.county_code:
            # constituency_data['County'] = constituency.county.name

            for i in s:
                output.append(s)
                constituency_data[constituency.county.name] = output
                print(output)
    response.append(constituency_data)
    return jsonify({"Constituencies": response})
    return jsonify({"status": "ok"})


@main.route('/governors', methods=['GET'])
# @token_required
def get_governors():
    # county=County.query.get(id)

    governors = Governor.query.all()

    output = []

    for governor in governors:
        governor_data = {}
        if governor.county_code:
            governor_data["county_code"] = governor.county.id
            governor_data["county"] = governor.county.name
            governor_data["id"] = governor.id
            governor_data["Governor"] = governor.surname + \
                " " + governor.othernames
            governor_data["Party"] = governor.party.name
        output.append(governor_data)
    return jsonify({"Governors": output})

    return jsonify({"Status": "ok"})


@main.route('/deputygovernors', methods=['GET'])
# @token_required
def get_deputygovernors():
    # county=County.query.get(id)

    deputygovernors = DeputyGovernor.query.all()

    output = []

    for deputygovernor in deputygovernors:
        deputygovernor_data = {}
        if deputygovernor.county_code:
            deputygovernor_data["county_code"] = deputygovernor.dpgovernor.id
            deputygovernor_data["county"] = deputygovernor.dpgovernor.name
            deputygovernor_data["id"] = deputygovernor.id
            deputygovernor_data["Governor"] = deputygovernor.governor.surname + \
                " " + deputygovernor.governor.othernames
            deputygovernor_data["Deputy Governor"] = deputygovernor.surname + \
                " " + deputygovernor.othernames
            deputygovernor_data["Party"] = deputygovernor.party.name
        output.append(deputygovernor_data)
    return jsonify({"Deputy Governors": output})

    return jsonify({"Status": "ok"})


@main.route('/senators', methods=['GET'])
# @token_required
def get_senators():
    # county=County.query.get(id)

    senators = Senator.query.all()

    output = []

    for senator in senators:
        senator_data = {}
        if senator.county_code:
            senator_data["county_code"] = senator.countysenator.id
            senator_data["county"] = senator.countysenator.name
            senator_data["id"] = senator.id
            senator_data["Senator"] = senator.surname + \
                " " + senator.othernames
            senator_data["Party"] = senator.party.name
        output.append(senator_data)
    return jsonify({"Governors": output})

    return jsonify({"Status": "ok"})


@main.route('/womenreps', methods=['GET'])
# @token_required
def woman_rep():
    # county=County.query.get(id)

    womanreps = WomanRep.query.all()

    output = []

    for womanrep in womanreps:
        womanrep_data = {}
        if womanrep.county_code:
            womanrep_data["county_code"] = womanrep.county.id
            womanrep_data["county"] = womanrep.county.name
            womanrep_data["id"] = womanrep.id
            womanrep_data["Woman Representative"] = womanrep.surname + \
                " " + womanrep.othernames
            womanrep_data["Party"] = womanrep.party.name
        output.append(womanrep_data)
    return jsonify({"County Women Representatives": output})

    return jsonify({"Status": "ok"})


# @main.route('/login')
# def login():
#     auth =request.authorization

#     if not auth  or not auth.username or not auth.password:
#         return make_response("could not verify",401,{'WWW-Authenticate':'Basic realm="Login required!"'})

#     user=User.query.filter_by(name=auth.username).first()

#     if not user:
#          return make_response("could not verify",401,{'WWW-Authenticate':'Basic realm="Login required!"'})

#     if check_password_hash(user.password,auth.password):
#         token=jwt=encode({'public_id':user.public_id,'exp': datetime.datetime.utcnow()+ datetime.timedelta(minutes=30) app.config['SECRET_KEY']})
#         return jsonify({'token':token.decode('UTF-8')})
#     return make_response("could not verify",401,{'WWW-Authenticate':'Basic realm="Login required!"'})


@main.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'secret':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(seconds=15)}, app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
