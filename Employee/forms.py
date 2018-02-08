from django import forms

from .models import Employee, Department
from django.utils.translation import ugettext_lazy as _


class EmployeeSignUpForm(forms.ModelForm):
    username = forms.RegexField(regex=r'^\w+$',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'required': 'True',
                                                              'max_length': 30,
                                                              'placeholder': 'نام کاربری',
                                                              'style': 'text-align:right'}
                                                       ),
                                label=_("نام کاربری"),
                                error_messages={
                                    'invalid': _("تنها استفاده از حروف انگلیسی، اعداد و _ در نام کاربری مجاز است."),
                                    'required': _('لطفا نام کاربری را وارد کنید')})
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'required': 'True',
                                                                  'max_length': 30,
                                                                  'render_value': 'False',
                                                                  'placeholder': 'رمز عبور',
                                                                  'style': 'text-align:right'}
                                                           ),
                                label=_("رمز عبور"),
                                error_messages={
                                    'required': _('لطفا رمزعبور را وارد کنید')
                                })
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'required': 'True',
                                                                  'max_length': 30,
                                                                  'render_value': 'False',
                                                                  'placeholder': 'تکرار رمز عبور',
                                                                  'style': 'text-align:right'}
                                                           ),
                                label=_("تکرار رمز عبور"),
                                error_messages={
                                    'required': _('لطفا رمزعبور را تکرار کنید')
                                })

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'employee_id']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'نام',
                                                 'style': 'text-align:right'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'نام خانوادگی',
                                                'style': 'text-align:right'}),
            'email': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'ایمیل',
                                            'style': 'text-align:right'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'شماره تماس',
                                                   'style': 'text-align:right'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'شماره کارمندی',
                                                 'style': 'text-align:right'})
        }
        labels = {
            'first_name': _('نام'),
            'last_name': _('نام خانوادگی'),
            'email': _('ایمیل'),
            'phone_number': _('شماره تماس'),
            'employee_id': _('شماره کارمندی'),
        }
        error_messages = {
            'first_name': {
                'required': _('لطفا نام را وارد کنید')
            },
            'last_name': {
                'required': _('لطفا نام خانوادگی را وارد کنید')
            },
            'email': {
                'required': _('لطفا ایمیل را وارد کنید'),
                'invalid': _('ایمیل اشتباه است')
            },
            'phone_number': {
                'required': _('لطفا شماره تلفن را وارد کنید'),
                'invalid': _('شماره تلفن اشتباه است')
            },
            'employee_id': {
                'required': _('لطفا شماره کارمندی را وارد کنید'),
                'invalid': _('شماره کارمندی نامعتبر است')
            }
        }

    def clean(self):
        cleaned_data = super(EmployeeSignUpForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('رمزعبور یکسان نیست')
        return cleaned_data




class AddDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'department_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'نام پروسه',
                                                'style': 'text-align:right'}),
            'department_id': forms.NumberInput(attrs={'class': 'form-control',
                                           #'placeholder': 'نام پروسه',
                                           #'style': 'text-align:right'
                                                      })
        }

        labels = {
            'name': _('نام پروسه'),
            'department_id': _('کد شرکت'),
        }



class EmployForm(forms.ModelForm):
    employee_id = forms.RegexField(regex=r'^\d+$',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'required': 'True',
                                                              'max_length': 30,
                                                              'placeholder': 'شماره کارمندی',
                                                              'style': 'text-align:right'}
                                                       ),
                                label=_("شماره کارمندی"),
                                error_messages={
                                    'invalid': _("تنها استفاده از اعداد در شماره کارمندی مجاز است."),
                                    'required': _('لطفا شماره کارمندی را وارد کنید')})


class FireForm(forms.ModelForm):
    employee_id = forms.RegexField(regex=r'^\d+$',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'required': 'True',
                                                              'max_length': 30,
                                                              'placeholder': 'شماره کارمندی',
                                                              'style': 'text-align:right'}
                                                       ),
                                label=_("شماره کارمندی"),
                                error_messages={
                                    'invalid': _("تنها استفاده از اعداد در شماره کارمندی مجاز است."),
                                    'required': _('لطفا شماره کارمندی را وارد کنید')})


class SetManagerForm(forms.ModelForm):
    employee_id = forms.RegexField(regex=r'^\d+$',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'required': 'True',
                                                              'max_length': 30,
                                                              'placeholder': 'شماره کارمندی',
                                                              'style': 'text-align:right'}
                                                       ),
                                label=_("شماره کارمندی"),
                                error_messages={
                                    'invalid': _("تنها استفاده از اعداد در شماره کارمندی مجاز است."),
                                    'required': _('لطفا شماره کارمندی را وارد کنید')})


class EmployeePerformTaskForm(forms.ModelForm): # TODO change it in order to be able to retrieve all the answers
    paid = forms.IntegerField (#regex=r'^\w+$',
                                widget=forms.NumberInput(attrs={'class': 'form-control',
                                                              'required': 'True',
                                                              'max_length': 30,
                                                              #'placeholder': 'preprocess name',
                                                              #'style': 'text-align:right'
                                                                }
                                                       ),
                                label=_("paid"),
                                #error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")}
                                )



class AddTaskForm(forms.ModelForm):
    process_bp = forms.RegexField(regex=r'^\d+$',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'required': 'True',
                                                              'max_length': 30,
                                                              'placeholder': 'نام پروسه',
                                                              'style': 'text-align:right'}
                                                       ),
                                label=_("نام پروسه"),
                                error_messages={
                                    'invalid': _("تنها استفاده از اعداد در شماره کارمندی مجاز است."),
                                    'required': _('لطفا نام پروسه را وارد کنید')})
    student_id = forms.IntegerField (#regex=r'^\w+$',
                                widget=forms.NumberInput(attrs={'class': 'form-control',
                                                              'required': 'True',
                                                              'max_length': 30,
                                                              #'placeholder': 'preprocess name',
                                                              #'style': 'text-align:right'
                                                                }
                                                       ),
                                label=_("student_id"),
                                #error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")}
                                )
