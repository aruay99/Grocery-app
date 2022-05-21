var productListApiUrl = 'http://127.0.0.1:5000/getProducts';
var uomListApiUrl = 'http://127.0.0.1:5000/getUOM';
var productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
var productDeleteApiUrl = 'http://127.0.0.1:5000/deleteProduct';
var orderListApiUrl = 'http://127.0.0.1:5000/getAllOrders';
var orderSaveApiUrl = 'http://127.0.0.1:5000/insertOrder';

$(function () {
  //Json data by api call for order table
  $.get(orderListApiUrl, function (response) {
      if(response) {
          var table = '';
          var totalCost = 0;
          $.each(response, function(index, order) {
              totalCost += parseFloat(order.total);
              table += '<tr>' +
                  '<td>'+ order.datetime +'</td>'+
                  '<td>'+ order.order_id +'</td>'+
                  '<td>'+ order.customer_name +'</td>'+
                  '<td>'+ order.total.toFixed(2) +' Rs</td></tr>';
          });
          table += '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>'+ totalCost.toFixed(2) +' Rs</b></td></tr>';
          $("table").find('tbody').empty().html(table);
      }
  });
});