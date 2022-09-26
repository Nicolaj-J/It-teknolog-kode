name = input('Name of the victim ? ')
str = """Most highly esteemed $XXX.We have the incredible pleasure of introducing 
you to out new series of products for the discerning customer. 
As you, $name, is known as one who only goes for the best of the best, 
please allow us to offer you a personal introductory discount.In order 
for you to make use of this irresistable discount, $XXX, it is vital 
that you enter your full name, your visa account number and this code:542XS3486Q-9, 
when you order from us.We are looking forwards to making you, $XXX, a regular and 
esteemed customer.Carl Smart. CEO, Dan-junc."""

str = str.replace( '$XXX', name)
print(str)