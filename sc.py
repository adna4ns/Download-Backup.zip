#by mr.13u4y4l4ut > KID2ZON3 
#copyright @2018

import httplib
import socket
import sys

try:
    print "    "
    print "     "
    print "  **********************************************"
    print " |                                             |"
    print " |                                             |"
    print " |    Auto Scanner Download Backup Zip         |"                       
    print " |<> Anon Cyber Team <> N45HT <> IndoXploit <> |"
    print " |     Special Thanks To Mr.13u4y4l4ut         |"
    print " |                                             |"                         
    print "  ********************************************** "
    var1=0
    var2=0

    php = ['backup-web.zip','blogz.ip','blog.sql','ssl_check.zip','tar.zip','search.zip','2018.zip','blog-backup.zip','bloog-backup.sql','backup.sql','backupweb.zip','bin.zip','web.zip','website.zip','2018.zip','tahunlama.zip','tahunkemarin.zip','kemarin.zip','wordpress.zip','images.zip','under.zip','files.zip','file.zip','admin.zip','app.zip','apps.zip','sql.zip','db.zip','web-lama.zip','bulan-lalu.zip','cpanel.zip','cp.zip','user-zip','email.zip','web-backup.zip','adminweb.zip','wp.zip','joomla.zip','inidia.zip','ini-dia.zip','berdoa.zip','amin.zip','ini-admin.zip','admin-backup.zip','backup-admin.zip','website.zip','seluruhwebsite.zip','seluruhwebsiteini.zip','allwebsite.zip','wordpress.zip','backup-wordpress.zip','jdih.zip','kominfo.zip','kemkominfo.zip','polisi.zip','undangan.zip','kartu-website.zip','emailwebsiteini.zip','emailwebsiteini.txt','jdih-web.zip','configuration.zip','sitemap.zip','upload.zip','backup.zip','filebackup.zip','fileadmin.zip','admin.zip','wp-content.zip','untukadmin.zip','backuppp.zip','ini-backup-web.zip','website-backup.zip','wp-admin.zip','cgi-bin.zip','jkt.zip','website.zip','joomla.zip','administrator.zip','wp-content.zip','wp-backup.zip','backup/backup-web.zip','backup/web.zip','backup/web-backup.zip','backup/wordpress.zip','backup','backup/joomla-backup.zip','backup/jdih.zip','backup-2017-12-13.zip','backupweb-2017.zip','web-2017.zip','backup-website-12.zip','conig.zip','wp-content/functions.zip','wp-settings.zip','xmlrpc.zip','wp-user.zip','themes-web.zip','themes-website.zip','themes-website-2017.zip','tema.zip','temawebsite.zip','temawebsitebaru.zip','inibackup.zip','ini-file-backup.zip','fileweb.zip','filewebsite.zip','file-website-2017.zip','backupweblama.zip','weblama.zip','backupweblama.zip','backup-an-webini.zip','ini-dia.zip','gw-capek.zip','tambahin-list-nya-sendiri-yaa.zip','masih-banyak-kok.zip','adminweb.zip','website.zip','website-backup.zip','backupp.zip','untuk-admin.zip','lupa.zip','administrator-user.zip','tm.zip','log.zip','media.zip','admin-joomla.zip','admin-ganteng.zip','admin-gans.zip','admin-user.zip','wp-login.zip','ingetin.zip','wp-admin.zip','wp-includes.zip','css.zip','configweb.zip','website-config.zip','gueee-capekkkk.zip','login.zip','2017-12.zip','desember.zip','januari.zip','februari.zip','maret.zip','april.zip','mei.zip','juni.zip','juli.zip','wellknown.zip','well-known.zip','adminlogin.zip','backup-admin.zip','backup-wp-content.zip','wp-admin.zip','backup-site.zip','website-backup.zip','under.zip','maintenance.zip','perbaikan.zip','upgrade.zip','update.zip','update-website-12.zip','website-upgrade.zip','xmlrpc.zip','plugins.zip','backup-index.php.zip','hariini.zip','hari-ini.zip','.well-known.zip','adminganteng.zip','ganteng-admin.zip','location.zip','wp-admin.zip','config/koneksi.zip','-ff.zip','config/database.zip','backupppp.zip','backuplama.zip','backupweblama.zip','indexlama.zip','lamaindex.zip','create-update.zip','haladmin.zip','config.zip','login.zip','loginwebsite.zip','websitelogin.zip','backup-admin.zip','adminlama-backup.zip','lama-backupadmin.zip','idulfitri.zip','bulan-kemarin.zip','email.zip','email.txt','perhatikaninidahulu.txt','warning.txt','peringatan.zip','peringatan.txt','bacainidulu.txt','pleasebacaini.txt','agustus.zip','september.zip','oktober.zip','november.zip','backuplama.zip','2015.zip','ok-sekian.zip','backup/filebackup.zip','backup/user.zip','backup/adminweb.zip','adminweb/adminweb/zip','panel/panel.zip','database.sql','file.sql','backup-web.rar','jdih.sql','file-pengguna.sql','user.sql','admin.sql','wordpress.sql','okee-sekiaan.zip','gw-capek.zip']
    try:
        print"    "
        site = raw_input("Website Kentod >> ")
        site = site.replace("http://","")
        conn = httplib.HTTPConnection(site)
        conn.connect()
        print "      "
        print "\t[$] Website Yang Dimasukkan Benar."
    except (httplib.HTTPResponse, socket.error) as Exit:
        raw_input("[!] Pake Internet Goblog / URL yang dimasukin salah; Please Enter To Continue")
        exit()
    print "   "
    print "1 zip"
    print "\nPress Number and 'Enter key' for Select Zip\n"
    code=input("> ")    

    if code==1:   
        print("\t [+] Scanning to Website >>> " + site + "...\n\n")
        for admin in php:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print "       "
            print ("\t >>> " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ( "\n\n>>>" + host, "Files Zip Found !!!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (host, " Interesting response:", response.status)
            connection.close()
        print("\n\nCompleted \n")
        print var1, " File Backup Zip Found"
        print var2, " Total Scanner"
        raw_input("[!] See You Next Time, Press Enter to Exit")

except (httplib.HTTPResponse, socket.error):
    print "\n\t[!] Session Cancelled; Error occured. Check internet settings"
except (KeyboardInterrupt, SystemExit):
    print "\n\t[!] Scan Dibatalkan karna Koneksi Internet Lo jelek"