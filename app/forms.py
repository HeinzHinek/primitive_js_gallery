# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectField, HiddenField
from wtforms import validators


class LoginForm(Form):
    nickname = StringField(u'ユーザ名', [validators.data_required()])
    password = PasswordField(u'パスワード', [validators.data_required(),
                                        validators.length(min=5, max=30)])
    submit = SubmitField(u'ログイン')


class AddUserForm(Form):
    nickname = StringField(u'ユーザー名', [validators.data_required()])
    role = SelectField(u'権限', coerce=int)
    password = PasswordField(u'パスワード', [validators.data_required(),
                                        validators.length(min=5, max=30),
                                        validators.equal_to('password_check',
                                                            message=u'確認用のパスワードが違っています。')])
    password_check = PasswordField(u'パスワードの確認', [validators.data_required(),
                                                 validators.length(min=5, max=30)])
    submit = SubmitField(u'登録')


class EditUserForm(Form):
    nickname = StringField(u'ユーザー名', [validators.data_required()])
    role = SelectField(u'権限', coerce=int)
    submit = SubmitField(u'保存')


class PasswordChangeForm(Form):
    old_password = PasswordField(u'既存のパスワード',
                                 [validators.data_required(),
                                  validators.length(min=5, max=30)])
    new_password = PasswordField(u'新しいパスワード',
                                 [validators.data_required(),
                                  validators.length(min=5, max=30),
                                  validators.equal_to('new_password_confirm',
                                                      message=u'新しいパスワードと確認用のパスワードが一致していません！')])
    new_password_confirm = PasswordField(u'パスワードの確認',
                                         [validators.data_required(),
                                          validators.length(min=5, max=30)])
    submit = SubmitField(u'変更')


class SimpleHiddenForm(Form):
    hidden = HiddenField()
