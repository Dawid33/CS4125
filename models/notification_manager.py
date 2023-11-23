from models.notification import EmailDecorator, Notification, SmsDecorator

class NotificationManager():

    def send_book_borrow_confirmation(self, email, book_title):
        msg = f"""
        You have successfully borrowed {book_title}. 
        Thank you for using our services.

        Kind Regards,
        Library Management Team."""
        notification = Notification(msg)
        notification = EmailDecorator(notification, "Succesfully borrowed book!")
        notification = SmsDecorator(notification)
        notification.send(email)

    def send_book_return_confirmation(self, email, book_title):
        msg = f"""
        You have successfully returned {book_title}. 
        Thank you for using our services.

        Kind Regards,
        Library Management Team."""
        notification = Notification(msg)
        notification = EmailDecorator(notification, "Succesfully returned book!")
        notification = SmsDecorator(notification)
        notification.send(email)

