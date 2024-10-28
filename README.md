<p align = 'center'> <img src = "https://github.com/user-attachments/assets/9f901765-015d-445e-8c26-a28d6fbd43f8"> </p>






A solution to data breaches in Cloud Computing. The proposed model aims to enhance the security of data stored by encrypting the data, fragmenting it, and securely exchanging a key, the model offers enhanced security and privacy for sensitive data.



Data security is a critical issue in cloud computing due to the sensitive nature of the information stored and processed in the cloud. The following are some of the reasons why data security is important in cloud computing:
• Sensitive Information: Many organizations store and process sensitive information, such as personal and financial information, in the cloud. This information is vulnerable to unauthorized access, theft, and misuse if it is not properly secured.
• Compliance Requirements: Regulations such as the General Data Protection Regulation (GDPR) and the Health Insurance Portability and Accountability Act (HIPAA) require organizations to protect personal data and ensure data security.
• Reputation: Data breaches can damage an organization's reputation and result in loss of trust from customers and other stakeholders.
• Cost: Data breaches can result in significant financial losses, such as legal costs, compensation payments, and lost business.
• Business Continuity: Data security is essential to ensure the availability and integrity of information, which is critical for the continuous operation of business processes.

Therefore, it is crucial for organizations to implement robust data security measures when using cloud computing services. This includes encryption of data, secure authentication, access control, and regular backups to protect against data loss. Organizations should also conduct regular security assessments and audits to ensure that their data is secure and to identify and address any potential security risks.
    
    
We, the authors of Project NOルVA have proposed a solution to data breaches in Cloud Computing. The proposed model aims to enhance the security of data storage and management in cloud computing. The model starts by taking data and a form of identity from a user and sending it to a cloud platform. The data is then encrypted using the identity provided, which serves as the encryption key. The encrypted data is then fragmented, and each fragment is stored in a different location. To further enhance the security of the data, a key exchange is performed between the user and the cloud platform using the Diffie-Hellman key exchange protocol. This protocol allows the two parties to securely generate a shared secret key that can be used for encryption and decryption. In this case, the key generated is used to encrypt the location of the fragments. This encrypted location information is then sent back to the user.

To retrieve the data, the user must provide the cloud platform with their identity and the encrypted location information. Upon receipt of the identity and encrypted location information, the cloud platform can use the Diffie-Hellman key exchange protocol to securely generate the shared secret key. This key can then be used to decrypt the encrypted location information, which reveals the locations of the fragments. The user can then retrieve the fragments and use their identity to decrypt the data.

The proposed model offers several advantages over traditional methods of data storage and management in cloud computing. First, by encrypting the data and the location of the fragments, the security of the data is enhanced. Second, by fragmenting the data and storing each fragment in a different location, the model reduces the risk of data loss or corruption. Third, by using the Diffie-Hellman key exchange protocol, the model provides an additional layer of security, as the shared secret key is generated in a secure manner and can only be decrypted by the user.

In conclusion, the proposed model provides a secure and efficient method of data storage and management in cloud computing. By encrypting the data, fragmenting it, and securely exchanging a key, the model offers enhanced security and privacy for sensitive data. This can be particularly useful for organizations that require secure storage and management of sensitive data in the cloud.

It is requested for all users to note that Project NOルVA was originally initiated as a project material for a course (Information Security Management) at our university. However, we plan to further our research in this topic and continue to provide regular updates to NOルVA.
