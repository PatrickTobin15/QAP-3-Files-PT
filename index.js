  // Desc: Mo's Lawncare Services - Customer Invoice
  // Author: Patrick Tobin
  // Date: July 16, 2025
  window.onload = function() {

  // Defining the program's constants here
  const BRD_PERC = 0.04;            // 4 percent of the border is the total square footage.
  const BRD_RATE = 0.35;           // $0.35 for the border per square foot.
  const LWN_RATE = 0.072;           // $0.072 per square foot of the lawn mowed.
  const FRT_RATE = 0.027;           // $0.027 per square foot for the amount of fertilizer.
  const HST_RATE = 0.15;           // 15% is the tota for the HST tax.
  const ENV_TAX = 0.014;          // 1.4% is the total for the environmental tax.

  // The main program is starting here

  // Collecting the customers inputs
  let custName = prompt("What is the customer's name?:                                          ");
  let strtAdd = prompt("What is the street address of the property being serviced?:             ");
  let cityPhn = prompt("Which City is it and what is the Phone Number?                          ");
  let propSize = prompt("What is the property size in Square Feet?                              ", 1000);
  propSize = parseFloat(propSize); // This will convert from a string to a number

  // The program is beginning to perform the calculations.
  
  // Starting out by getting the border size in order to calculate the cost of it
  let brdArea = propSize * BRD_PERC;
  let brdCost = brdArea * BRD_RATE;

  // The remaining area of the lawn and the total cost of mowing it, reminder this is after the border.
  let lwnArea = propSize - brdArea;
  let mowCost = lwnArea * LWN_RATE;

  // The cost of the fertilizer for the entire property.
  let fertCost = propSize * FRT_RATE;

  // The subtotal before the taxes take affect
  let subtot = brdCost + mowCost + fertCost;

  // The taxes
  let hst = subtot * HST_RATE;
  let envirTax = subtot * ENV_TAX;

  // The total cost invoice
  let totInv = subtot + hst + envirTax;

  // Displaying the results inside the HTML
  document.getElementById("custDetails").innerHTML = `
    ${custName}
    ${strtAdd}
    ${cityPhn}
    `;

  document.getElementById("propSize").textContent = propSize.toFixed(2);
  document.getElementById("bordCost").textContent = "$" + brdCost.toFixed(2);
  document.getElementById("mowCost").textContent = "$" + mowCost.toFixed(2);
  document.getElementById("fertCost").textContent = "$" + fertCost.toFixed(2);
  document.getElementById("subtot").textContent = "$" + subtot.toFixed(2);
  document.getElementById("hst").textContent = "$" + hst.toFixed(2);
  document.getElementById("envirTax").textContent = "$" + envirTax.toFixed(2);
  document.getElementById("totalInv").textContent = "$" + totInv.toFixed(2);
};
