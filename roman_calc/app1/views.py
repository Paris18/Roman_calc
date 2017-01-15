from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import re
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


def roman_to_no(n):
	roman_value = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	n = n.upper()
	total = 0
	while n:
		if len(n) == 1 or roman_value[n[0]] >= roman_value[n[1]]:
			total += roman_value[n[0]]
			n = n[1:]
		else:
			total += roman_value[n[1]] - roman_value[n[0]]
			n = n[2:]
	return total

def no_to_roman(n):
	if n == 0:
		return "None"
	# if n % 1 != 0 :
	# 	print "roman does not support for fractions"
	# 	return 
	returnstring=''
	roman_value = [['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
	for i in roman_value.values():
		while n - i[1] >= 0:
			n -= i[1]
			returnstring += i[0]
	return returnstring

import json


@csrf_exempt
def roman_clc(request):
	print "hi"
	# if request.method == 'GET':
	# 	return render(request, "roman.html",{})
	# if request.POST:
	# print "hi"
	qry = json.loads(request.body)
	print qry["qriy"]

	k = qry["qriy"]
		# qry = "IX + X"
	ab = re.compile(r'[IVXLCDM]+([\+|\-|\*|\/|%][IVXLCDM]+)+')
	if not ab.match(k):
		return HttpResponse("Wrong formate of roman Expression-----/\n Roman Number Containce only IVXLCDM \n ex: IX+X ")
	oprtr = re.sub(r'[IVXLCDM]','',k).strip()
	# roman_no = ['I','X','V','X','L','C','D','M']
	qryl = [x.strip() for x in k.split(oprtr)]
	q = str(roman_to_no(qryl[0])) + oprtr + str(roman_to_no(qryl[1]))
	''' for more than 3 parmeter like IX + X - I
	q = str(roman_to_no(qryl[0]))
	for i in range(1,len(qrly)):
		q += oprtr[i-1] + str(roman_to_no(qryl[i])) '''

	rst = eval(q)
	return HttpResponse(no_to_roman(rst))

