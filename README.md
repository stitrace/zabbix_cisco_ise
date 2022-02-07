Cisco ISE sessions zabbix monitoring template

That template can monitor only two parametrs - count of active endpoint sessions and number of authz in last 15 minutes (graph and alarm triggers added too). It work over REST api of Cisco ISE.

NOTE:
- cisco_ise_template-v2.4.xml - to Zabbix version <= 2.4
- cisco_ise_template-v3.0.xml - for Zabbix version >= 3.0

Installation:

1) Move ise.py into zabbix external scripts directory. Chown it to zabbix user/group and chmod 711 on it. 
2) Import XML template file into zabbix.
3) Pin template to ISE host in zabbix interface
4) Create monitor user in ISE.
5) Edit Macros values in zabbix Host configuration

