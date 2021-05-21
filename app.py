from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

papers_list = []
users_list = []

import papers
import users

if __name__ == '__main__':
   papers_list.append({'Paper Title':'Explaining and Harnessing Adversarial Examples','author':'Goodfellow et al.', 'citations':'6995', 'available':'True'})
   papers_list.append({'Paper Title':'Semi-Supervised Classification with Graph Convolutional Networks','author':'Kipf and Welling', 'citations':'7021', 'available':'True'})
   papers_list.append({'Paper Title':'Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks','author':'Radford et al.', 'citations':'8681', 'available':'True'})
   papers_list.append({'Paper Title':'Mastering the game of Go with deep neural networks and tree search','author':'Silver et al.', 'citations':'9621', 'available':'True'})
   papers_list.append({'Paper Title':'Human-level control through deep reinforcement learning','author':'Mnih et al.', 'citations':'13615', 'available':'True'})

   users_list.append({'name':'Abhijan Wasti', 'Papers Submitted':'2', 'Papers Downloaded':'1'})
   users_list.append({'name':'Prabesh Nepal', 'Papers Submitted':'1', 'Papers Downloaded':'3'})
   users_list.append({'name':'Muna Bhusal', 'Papers Submitted':'1', 'Papers Downloaded':'3'})

   app.run(debug = True)