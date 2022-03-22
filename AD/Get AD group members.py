#Get AD group members

import sys
import ldap

AD_SERVERS = [ '10.*.*.*', '10.*.*.*', '10.*.*.*']
AD_GROUP_FILTER = '(&(objectClass=GROUP)(CN=JIRAOOO,OU=Automation,OU=Groups,DC=bgelov,DC=ru))'
AD_BIND_USER = 'taskuser@bgelov.ru'
AD_BIND_PWD = '**********************'


# ldap connection
def ad_auth(username=AD_BIND_USER, password=AD_BIND_PWD, address=AD_SERVERS[0]):
	conn = ldap.initialize('ldap://' + address)
	conn.protocol_version = 3
	conn.set_option(ldap.OPT_REFERRALS, 0)

	result = True

	try:
		conn.simple_bind_s(username, password)
		print('Succesfully authenticated')
	except ldap.INVALID_CREDENTIALS:
		return "Invalid credentials", False
	except ldap.SERVER_DOWN:
		return "Server down", False
	except ldap.LDAPError.e:
		if type(e.message) == dict and e.message.has_key('desc'):
			return "Other LDAP error: " + e.message['desc'], False
		else:
			return "Other LDAP error: " + e, False

	return conn, result



def get_group_members(ad_conn, basedn=AD_USER_BASEDN):
	members = []
	ad_filter = AD_GROUP_FILTER.replace('{group_name}', group_name)
	result = ad_conn.search_s(basedn, ldap.SCOPE_SUBTREE, ad_filter)
	if result:
		if len(result[0]) >= 2 and 'member' in result[0][1]:
			members_tmp = result[0][1]['member']
			for m in members_tmp:
				email = get_email_by_dn(m, ad_conn)
				if email:
					members.append(email)
	return members
	


ad_conn, result = ad_auth()
if result:
  group_members = get_group_members(ad_conn)
  for m in group_members:
    print(m)

