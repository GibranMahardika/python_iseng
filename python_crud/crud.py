host = "localhost"
user = "admin_1"
passwd = "admin_1"

import mysql.connector as mysql

db = mysql.connect(
    host = host,
    user = user,
    passwd = passwd
)

cursor = db.cursor()
# ===========================================

# untuk membuat database
# cursor.execute("CREATE DATABASE db_test_1")

# untuk delete database
# cursor.execute("DROP DATABASE db_test_1")

# untuk menunjukkan database yang ada di mysql
# cursor.execute("SHOW DATABASES")

# ===========================================
db.database="db_test_1"
cursor.execute('''
    create table data_pelanggan(
               ID INT NOT NULL AUTO_INCREMENT,
               nama  VARCHAR(100),
               alamat TEXT NOT NULL,
               tanggal DATE,
               PRIMARY KEY (ID)
    );
''')
db.commit()

cursor.execute("SHOW TABLES")
data = cursor.fetchall()
print(data)