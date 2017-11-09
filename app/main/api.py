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
import os

# secret= os.environ.get["SECRET_KEY"] 

# def token_required(f):
#     @wraps(f)
#     def decorated(*args,**kwargs):
#         token=None

#         if 'x-access-token' in request.headers:
#             token=request.headers['x-access-token']
#         if not token:
#             return jsonify ({'message':'token is Missing!'}),401

#         try:
#             data = jwt.decode(token, secret)
#             current_user=User.query.filter_by(id=id).first()
#         except:
#             return jsonify({'message':'Token is Invalid!'}),401

#         return f(current_user,*args,**kwargs)

@main.route('/womenrep', methods=['GET'])
# @token_required
def woman_rep():
    # county=County.query.get(id)

    womanreps=WomanRep.query.all()

    output=[]

    for womanrep in womanreps:
        womanrep_data={}
        if womanrep.county_code:
            womanrep_data["county_code"] = womanrep.county.id
            womanrep_data["county"]=womanrep.county.name
            womanrep_data["id"] = womanrep.id
            womanrep_data["Woman Representative"] = womanrep.surname + " " + womanrep.othernames
            womanrep_data["Party"]=womanrep.party.name
        output.append(womanrep_data)
    return jsonify({"County Women Representatives":output})



    return jsonify({"Status":"ok"})

    
@main.route('/counties', methods=['GET'])
# @token_required
def counties_get():
    counties=County.query.all()
    constituencies=Constituency.query.all()

    output=[]

    for county in counties:
        county_data={}
        constituencies_data={}
        county_data["county name"]=county.name
        county_data["id"] = county.id
       
    

        output.append(county_data)

    return jsonify({"Counties":output})

@main.route('/counties/constituencies', methods=['GET'])
# @token_required
def get_constituencies():
    output=[]
    constituency_data={}
    constituenciez=Constituency.query.filter(Constituency.county_code>0).all()
    constituencies=Constituency.query.all()
    print(constituencies)
    for constituency in constituencies: 
        for constie in constituenciez:
            if constituency.county_code:
                s=[(constituency.county.name,constie.name)]
                d={}
                for k,v in s:
                    d.setdefault(k,[]).append(v)
                    print(d.items())
                    output.append(d)

    
    return jsonify({"Counties":output})
    return jsonify({"Status":"ok"})

    
        
     
    



# @main.route('/counties/constituenties', methods=['GET'])
# def constituenties_get():
#     constituenties=constituency.query.filter_by(constituency_code=>1)
   
#     output=[]

#     for constituency in constituenties:
#         consituenties_data={}
#         consituenties_data["id"] = consituenties.id
#         consituenties_data["counties"] = consituenties.name

#         output.append(county_data)

#     return jsonify({"Counties":output})



#     return jsonify({"Status":"ok"})

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