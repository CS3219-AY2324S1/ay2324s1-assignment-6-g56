const admin = require('firebase-admin');
const { onRequest } = require('firebase-functions/v2/https');

admin.initializeApp();

exports.addQuestion = onRequest((req, res) => {
    if (req.method === 'POST') {
        try {
          const data = req.body; // Data to be added to Firestore
          const firestore = admin.firestore();
          const documentRef = firestore.collection('questions').add(data);
  
          res.status(200).send({ success: true, id: documentRef.id });
        } catch (error) {
          console.error('Error adding document:', error);
          res.status(500).send({ success: false, error: error.message });
        }
      } else {
        // If not a POST request, return 405 - Method Not Allowed
        res.status(405).send({ success: false, message: 'Method not allowed' });
      }
});
