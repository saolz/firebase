import React from 'react';
import axios from "axios";

declare global {
  interface Window {
    Razorpay: any;
  }
}

interface RazorpayResponse {
  razorpay_payment_id: string;
  razorpay_order_id: string;
  razorpay_signature: string;
}

// ... existing imports ...

const RazorpayPayment: React.FC = () => {
  const handlePayment = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:8000/api/create-order/");
      console.log("Order created:", res.data);

      const options = {
        key: "rzp_test_xVdiKSkwDJsHoU",  // Updated to match your backend key
        amount: res.data.amount,
        currency: "INR",
        name: "Test Company",
        description: "Test Transaction",
        order_id: res.data.id,
        handler: function (response: any) {
          console.log("Payment success:", response);
          alert("Payment Successful!");
        },
        prefill: {
          name: "Test User",
          email: "test@example.com",
          contact: "9999999999"
        },
        theme: {
          color: "#3399cc"
        }
      };

      console.log("Opening Razorpay with options:", { ...options, key: "HIDDEN" });
      const paymentObject = new window.Razorpay(options);
      paymentObject.on('payment.failed', function (response: any){
        console.error("Payment failed:", response.error);
        alert("Payment Failed: " + response.error.description);
      });
      paymentObject.open();
    } catch (error) {
      console.error("Error:", error);
      alert("Error initiating payment. Please check console.");
    }
  };

  return <button onClick={handlePayment}>Pay Now</button>;
};

export default RazorpayPayment;