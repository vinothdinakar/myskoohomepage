#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2

from google.appengine.api import mail

import logging
logging.getLogger().setLevel(logging.DEBUG)


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])





class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'title': 'title'
        }

        homepage_template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(homepage_template.render(template_values))

class FeaturesPageHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'title': 'title'
        }

        homepage_template = JINJA_ENVIRONMENT.get_template('features.html')
        self.response.write(homepage_template.render(template_values))

class ContactPageHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'title': 'title'
        }

        homepage_template = JINJA_ENVIRONMENT.get_template('contact.html')
        self.response.write(homepage_template.render(template_values))

class AboutUsPageHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'title': 'title'
        }

        homepage_template = JINJA_ENVIRONMENT.get_template('about.html')
        self.response.write(homepage_template.render(template_values))

class LoginPageHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'title': 'title'
        }

        homepage_template = JINJA_ENVIRONMENT.get_template('login.html')
        self.response.write(homepage_template.render(template_values))

class GetEmailIdHandler(webapp2.RequestHandler):
    def get(self):
        email_id = self.request.get('email_id')

        if not mail.is_email_valid(email_id):
            # prompt user to enter a valid address
            logging.info('Invalid email address')

        else:
            self.sendEmail(email_id)
            self.sendMailToMyskoo(email_id)


        responseJson = '{"status":"success"}'
        self.response.write(responseJson)

    def sendMailToMyskoo(self, email_id):
        bodyText = """
              Hi Admin,

              User has sent a email id:
              Email: """ + email_id + """

              Thanks.
        """


        mail.send_mail(sender="Myskoo.in Support <admin@myskoo.in>",
                      to="contact@myskoo.in",
                      subject="Email id form user",
                      body=bodyText)

    def sendEmail(self, email_id):

        bodyText = """
              Hi,

              Thanks for your interest in Myskoo. One of our member from our support team will soon
              be contacting you. We will talk to you and get your requirements and will
              try to give you a better solution.
              You can also request for a demo from our support staff.

              Thanks,
              Anish Johnson,
              Chief Operational Manager.
              """

        mail.send_mail(sender="Myskoo.in Support <admin@myskoo.in>",
                      to=email_id,
                      bcc="Myskoo.in Support <admin@myskoo.in>",
                      subject="We got your email id",
                      body=bodyText)







class SendUsMessageHandler(webapp2.RequestHandler):
    def get(self):
        contact_name = self.request.get('contact_name')
        contact_phone_number = self.request.get('contact_phone_number')
        contact_email = self.request.get('contact_email')
        contact_message = self.request.get('contact_message')

        if not mail.is_email_valid(contact_email):
            # prompt user to enter a valid address
            logging.info('Invalid email address')

        else:
            self.sendEmail(contact_name, contact_email, contact_message)
            self.sendMailToMyskoo(contact_name, contact_email, contact_phone_number, contact_message)


        responseJson = '{"status":"success"}'
        self.response.write(responseJson)

    def sendMailToMyskoo(self, contact_name, contact_email, contact_phone_number, contact_message):
        bodyText = """
              Hi Admin,

              There is a message from user:
              Name : """ + contact_name + """
              Email: """ + contact_email + """
              Contact Number: """ + contact_phone_number + """
              Message: """ + contact_message + """

              Thanks.
        """


        mail.send_mail(sender="Myskoo.in Support <admin@myskoo.in>",
                      to="contact@myskoo.in",
                      subject="Message from user",
                      body=bodyText)

    def sendEmail(self, contact_name, contact_email, contact_message):

        template_values = {
            'title': 'title',
            'customer_name':contact_name
        }

        message = mail.EmailMessage(sender="Myskoo.in Support <admin@myskoo.in>",
                                    subject="We got your message")

        message.to = contact_email

        homepage_template = JINJA_ENVIRONMENT.get_template('basic.html')
        html_template = homepage_template.render(template_values)

        logging.info(html_template)

        message.body = """
        Dear """ + contact_name + """:

        Thanks for your interest in Myskoo. One of our member from our support team will soon
        be contacting you. We will talk to you and get your requirements and will
        try to give you a better solution.
        You can also request for a demo from our support staff.

        Thanks,
        Anish Johnson,
        Chief Operational Manager.
        """

        message.html = html_template

        message.send()


class RequestDemoHandler(webapp2.RequestHandler):
    def get(self):
        contact_name = self.request.get('name')
        contact_phone_number = self.request.get('phone')
        contact_email = self.request.get('email')

        if not mail.is_email_valid(contact_email):
            # prompt user to enter a valid address
            logging.info('Invalid email address')

        else:
            self.sendEmail(contact_name, contact_email)
            self.sendMailToMyskoo(contact_name, contact_email, contact_phone_number)

        responseJson = '{"status":"success"}'
        self.response.write(responseJson)

    def sendEmail(self, contact_name, contact_email):

        bodyText = """
              Dear """ + contact_name + """:

              Thanks for your interest in Myskoo. One of our member from our support team will soon
              be contacting you. We will talk to you and get your requirements and will
              try to give you a better solution.
              We will also arrange for a demo of our Myskoo application.

              Thanks,
              Anish Johnson,
              Chief Operational Manager.
        """


        mail.send_mail(sender="Myskoo.in Support <admin@myskoo.in>",
                      to=contact_email,
                      bcc="Myskoo.in Support <admin@myskoo.in>",
                      subject="We received your request for demo",
                      body=bodyText)

    def sendMailToMyskoo(self, contact_name, contact_email, contact_phone_number):
        bodyText = """
              Hi Admin,

              There is a request for a demo:
              Name : """ + contact_name + """
              Email: """ + contact_email + """
              Contact Number: """ + contact_phone_number + """

              Thanks.
        """


        mail.send_mail(sender="Myskoo.in Support <admin@myskoo.in>",
                      to="contact@myskoo.in",
                      subject="Request for demo",
                      body=bodyText)








app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
    ('/features', FeaturesPageHandler),
    ('/contact', ContactPageHandler),
    ('/aboutus', AboutUsPageHandler),
    ('/login', LoginPageHandler),
    ('/sendusmessage', SendUsMessageHandler),
    ('/getemailid', GetEmailIdHandler),
    ('/requestDemo', RequestDemoHandler),
], debug=True)
