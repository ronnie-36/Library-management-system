from flask import *
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL
import yaml
import hashlib

# modules
import models.librarian_section as librarian_section
import models.book_section as book_section
import models.user_section as user_section

app = Flask(__name__)
CORS(app)
app.secret_key = "abc"
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# Configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/portfolio-details', methods=['GET', 'POST'])
def portfoliodetails():
    return render_template('portfolio-details.html')

@app.route('/getStarted', methods=['GET', 'POST'])
def getStarted():
    return render_template('getStarted.html')



# librarian
app.add_url_rule('/librarian/login', view_func=librarian_section.librarian_login, methods=['GET','POST'])
app.add_url_rule('/librarian/logout', view_func=librarian_section.librarian_logout, methods=['GET'])
app.add_url_rule('/librarian/table', view_func=librarian_section.librarian_table, methods=['GET','POST'])
app.add_url_rule('/librarian/tab', view_func=librarian_section.librarian_tab_panel, methods=['GET','POST'])
app.add_url_rule('/librarian/home', view_func=librarian_section.librarian_home, methods=['GET','POST'])
app.add_url_rule('/librarian/add_librarian', view_func=librarian_section.librarian_add_librarian, methods=['GET','POST'])
app.add_url_rule('/librarian/download_employee', view_func=librarian_section.download_employee, methods=['GET'])
app.add_url_rule('/librarian/add_student', view_func=librarian_section.librarian_add_student, methods=['GET','POST'])
app.add_url_rule('/librarian/download_student', view_func=librarian_section.download_student, methods=['GET','POST'])
app.add_url_rule('/librarian/uploaded_student_files', view_func=librarian_section.uploaded_student_files, methods=['GET','POST'])
app.add_url_rule('/librarian/return-files-student/<filename>', view_func=librarian_section.return_files_student, methods=['GET'])
app.add_url_rule('/librarian/uploaded_librarian_files', view_func=librarian_section.uploaded_librarian_files, methods=['GET','POST'])
app.add_url_rule('/librarian/return-files-librarian/<filename>', view_func=librarian_section.return_files_librarian, methods=['GET'])
app.add_url_rule('/librarian/delete/student_forms/<sid>', view_func=librarian_section.delete_student_forms, methods=['GET'])
app.add_url_rule('/librarian/delete/librarian_forms/<lid>', view_func=librarian_section.delete_librarian_forms, methods=['GET','POST'])
app.add_url_rule('/librarian/add_books', view_func=librarian_section.librarian_add_books, methods=['GET','POST'])
app.add_url_rule('/librarian/add_shelf', view_func=librarian_section.librarian_add_shelf, methods=['GET','POST'])
app.add_url_rule('/librarian/deny/hold/<user_id>/<isbn>', view_func=librarian_section.deny_hold, methods=['GET'])
app.add_url_rule('/librarian/deny/issue/<user_id>/<isbn>', view_func=librarian_section.deny_issue, methods=['GET'])
app.add_url_rule('/librarian/accept/hold/<user_id>/<isbn>', view_func=librarian_section.accept_hold, methods=['GET'])
app.add_url_rule('/librarian/accept/issue/<role>/<user_id>/<isbn>', view_func=librarian_section.accept_issue, methods=['GET'])
app.add_url_rule('/librarian/requests', view_func=librarian_section.librarian_requests, methods=['GET','POST'])
app.add_url_rule('/librarian/manage', view_func=librarian_section.librarian_manage, methods=['GET','POST'])
app.add_url_rule('/librarian/delete/hold/<user_id>/<isbn>', view_func=librarian_section.delete_return_hold, methods=['GET'])
app.add_url_rule('/librarian/delete/issue/<user_id>/<isbn>', view_func=librarian_section.delete_return_issue, methods=['GET', 'POST'])
app.add_url_rule('/librarian/reload', view_func=librarian_section.reload, methods=['GET'])

# books
app.add_url_rule('/books/home', view_func=book_section.books_home, methods=['GET','POST'])
app.add_url_rule('/books/shelf/<shelf_id>', view_func=book_section.books_shelf_id, methods=['GET','POST'])
app.add_url_rule('/books/view-side/<shelf_id>/<title>', view_func=book_section.view_side, methods=['GET','POST'])
app.add_url_rule('/books/search/<title>', view_func=book_section.books_search_title, methods=['GET','POST'])
app.add_url_rule('/books/view-side-search/<search>/<title>', view_func=book_section.view_side_search, methods=['GET','POST'])
app.add_url_rule('/books/move/<shelf_id>/<title>', view_func=book_section.books_move_to, methods=['GET','POST'])
app.add_url_rule('/books/books_list_title/<title>', view_func=book_section.books_list_title, methods=['GET','POST'])
app.add_url_rule('/books/delete/<title>/<isbn>', view_func=book_section.books_delete, methods=['GET','POST'])
app.add_url_rule('/books/modify/<isbn>', view_func=book_section.books_modify, methods=['GET','POST'])
app.add_url_rule('/books/book_rating/<title>/<isbn>', view_func=book_section.books_rate, methods=['GET','POST'])
app.add_url_rule('/books/issue/<title>/<isbn>', view_func=book_section.books_issue, methods=['GET'])
app.add_url_rule('/books/hold/<title>/<isbn>', view_func=book_section.books_hold, methods=['GET'])
app.add_url_rule('/books/addinreadinglist/<isbn>', view_func=book_section.add_in_reading_list, methods=['GET','POST'])
app.add_url_rule('/books/addinpersonalbookshelf/<isbn>', view_func=book_section.add_in_personal_bookshelf, methods=['GET','POST'])

# user
app.add_url_rule('/user/login', view_func=user_section.user_login, methods=['GET','POST'])
app.add_url_rule('/user/logout', view_func=user_section.user_logout, methods=['GET'])
app.add_url_rule('/user/home', view_func=user_section.user_home, methods=['GET','POST'])
app.add_url_rule('/user/lists', view_func=user_section.reading_lists, methods=['GET','POST'])
app.add_url_rule('/user/lists/<url>', view_func=user_section.view_reading_list, methods=['GET','POST'])
app.add_url_rule('/user/friends', view_func=user_section.friends, methods=['GET','POST'])
app.add_url_rule('/user/friends/cr/<id>', view_func=user_section.friend_currentlyreading, methods=['GET','POST'])
app.add_url_rule('/user/friends/add', view_func=user_section.add_friend, methods=['GET','POST'])
app.add_url_rule('/user/bookshelves', view_func=user_section.bookshelves, methods=['GET','POST'])
app.add_url_rule('/user/bookshelves/<url>', view_func=user_section.view_personal_bookshelves, methods=['GET','POST'])

if __name__ == '__main__':
    flag = 0
    app.run(debug=True)
