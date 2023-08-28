# Define a function for sending emails with optional parameters.
def send_email(subject, body, **kwargs):
    # Get recipient's email address; use default if not provided.
    recipient = kwargs.get('recipient', 'info@example.com')

    # Get carbon copy (cc) recipients; default to an empty list if not provided.
    cc_recipients = kwargs.get('cc', [])

    # Get blind carbon copy (bcc) recipients; default to an empty list if not provided.
    bcc_recipients = kwargs.get('bcc', [])

    # Get attachments; default to an empty list if not provided.
    attachments = kwargs.get('attachments', [])

    # Simulate sending the email using print statements.
    print(f"Sending email with subject: '{subject}'")
    print(f"To: {recipient}")
    print(f"CC: {', '.join(cc_recipients)}")
    print(f"BCC: {', '.join(bcc_recipients)}")
    print(f"Attachments: {', '.join(attachments)}")
    print(body)


# Send a simple email
send_email('Hello', 'This is the email body.')

# Send an email with additional options
send_email(
    'Important News',
    'Please review the attached document.',
    recipient='john@example.com',
    cc=['alice@example.com', 'bob@example.com'],
    attachments=['report.pdf']
)

"""
1. The code defines a function named `send_email` that takes required arguments `subject` and `body`, 
along with optional keyword arguments using `**kwargs`.

2. The `recipient` argument is obtained from `kwargs`, using `'info@example.com'` as the default if not provided.

3. Similarly, `cc_recipients`, `bcc_recipients`, and `attachments` are obtained from `kwargs` with default values 
of empty lists if not provided.

4. The function simulates sending an email by printing out the email details and content.

5. A simple email is sent using the function with the subject `'Hello'` and the body `'This is the email body.'`.

6. Another email is sent with more options: subject `'Important News'`, body `'Please review the attached 
document.'`, `recipient`, `cc`, and `attachments` specified.

The provided code demonstrates how the `**kwargs` mechanism allows for flexible customization of the `send_email` 
function by providing optional parameters for recipient information, carbon copy recipients, blind carbon copy 
recipients, and attachments when sending emails.
"""
