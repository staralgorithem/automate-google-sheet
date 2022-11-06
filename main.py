import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets[{
  "type": "service_account",
  "project_id": "automate-sheet-367810",
  "private_key_id": "39837397ae50928dc9fea003490a07f8df0beb66",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDNBNRs8kZ29aO6\nUq+r3OtgZbGyfFJpR+tN+XuyTFEAyn6eK2AYRKzNEO08gJfq9y//PzWUykqpV3Gc\nU5T483+gkrvnmlDCR1cIdob5zRYnW4H19Fm+7r8O08IQHOE9ts8HxLjLMe7QnWit\nVSMSs7LGaRCIsJfDa6xOS4uGR3bn4/4sicfGTdQePRjRjqm8ArATEiKzIDGg5uOP\nVHbGxN9kmQ/Yo8oM/m4CFxtEPSoU1pza64JMVRoq5ApuxiOWuZ2mzVRPbrEJAnH4\n6AMlhDhDI/VeYNUPvl434a3QujPZX7Rjj5kHPs2ZNF4krlhC/BDNkHJFtIn/w8hB\nGG91N8/JAgMBAAECggEAA355fqmACm8kHRzjeg7FOIAbL8MfJhoFQwUFYZPxOHh7\nAR0/oWzq3gF+bY7KfVpnnWvEG8Gj1UV/KJkjEOgYzNGGCsvY5FVna2aWZSOkj5in\nZcabkJ23MLHqsjAaevJb470WTNOQcfU7eg1upYGzAl8lhT2Ej0kikgtcY3Y3Kvtd\nA9m2KfcJ3ez0NZBPEa/AtEIuKly2vlaHyLVB8Ldlt6qiBPWi+7muY5rJcv3SLrjo\nCvL7kbCN5EbT3Ik2syRXmfstf8CRZG1D97qAjLNrOrFHlcUoH5WqdjOnXkyYTEsp\nMJHv9ILLk1rvfM/y36i6Ehzf6FidhBrBFBA0A4OnFQKBgQDnNO1ECh19f4cCgR3v\n1Upz5xok0VoSe710Q5NYRV9n3BP+71iYq1UBRYLnvgtaCz8L7a0H2+tO6c6Q3fhe\nQeXFNkbCw4LEdpouFkdM2tthrNgnwasKD47dKZeTTi607o0SHxSs4ihP9zo9DKWg\nDh6wDjUcQxmrkT3dOmIhGE931QKBgQDjAP60l1YZi7Wd8NIRjZnLl7OEDRUnNnEq\njpORwxS59968skme5T5carabhK5YIrUhOUHMKuYAxgdAcvidp7Z4iiun95fZoC45\niMmPmvusN2d9/bjQ7Hv4gChRfbiRrhzXitXVaIy4Y39tazYAcBcuBBKd6Pec4wK3\nDuYdh/qGJQKBgE54fSrBkB6/ALCN5/41Uu6hehMS5tItIzDpmoG0EdxrKnI1A8nV\nJKWo1PQYYTvvYzeGNFrdfjCrVAuA+sHq9bQIZt3Fg4Vwh4Wq1Ao2oYy2ICrmJUnl\n2+QeMK6zM1D/QevrlpXSsEHrs91yhGgdQrcYK1hrQbQkOG30WcfHu3j9AoGABFKg\nhw/as+HVM4zCc1Me+qGI6ZrWLEj9HrJYXQ459tChjTZX8I6tAVWG5K9CIquGh3tv\npVOrzZf3y2JlGZt3/hOjgS9V1O8X8kCIlhN9d2oWrm+GdXQLaFAIdITQXvXR1sju\nCYJUK665XnwMKzX3OwkY0aj+Dh7EjnfaKfXM74ECgYAo/X4XdGRffUwe5kcXbFYB\nFU+UrqHudlEwlYnoxlBh7KLiX8XWn+4r8olRxWGm0N0LlEnFoFIKVHv6AF/7uGrw\nrPXGnzQ8UUQSDtZ247CpTA+yyofkPv33EAujoxbvZdUZFaQrmAb54YxprDYQ6FsO\ne54bdUxmkXlNEEj9HiAXDw==\n-----END PRIVATE KEY-----\n",
  "client_email": "service-acc@automate-sheet-367810.iam.gserviceaccount.com",
  "client_id": "106629800007559050268",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/service-acc%40automate-sheet-367810.iam.gserviceaccount.com"
}
],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["https://docs.google.com/spreadsheets/d/12345/edit?usp=sharing"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")
