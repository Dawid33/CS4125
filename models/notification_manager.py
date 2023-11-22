from models.notification import EmailNotification, Notification

class NotificationManager():

    def send_book_borrow_confirmation(self, email, book_title):
        msg = f"""
        You have successfully borrowed {book_title}. 
        Thank you for using our services.

        Kind Regards,
        Library Management Team."""
        notification = EmailNotification(Notification(msg))
        notification.send_with_subject(email, "Succesfully borrowed book!")

    def send_book_return_confirmation(self, email, book_title):
        msg = f"""
        You have successfully returned {book_title}. 
        Thank you for using our services.

        Kind Regards,
        Library Management Team."""
        notification = EmailNotification(Notification(msg))
        notification.send_with_subject(email, "Succesfully returned book!")

