// function convert_format(user_date) {
//     a = user_date.split('/')
//     var first = a[0] 
//     a[0] = a[a.length - 1]
//     a[a.length - 1] = first
//     return a.join('')

// }

// convert_format('10/10/2015')


// function ensure(value) {
//     // Your code goes here
//     if (value === undefined || value === '' || value === NaN) {
//         throw "error"
//     }
//   }
  
//   try {
//     console.log(ensure());
//   } catch(err) {
//     console.log(err);
//   }


// function removeProperty(obj, prop) {
//   if (prop in obj) {
//     delete obj[prop]
//     return true
//   }
//   return false
// }

function formatDate(userDate) {
    // format from M/D/YYYY to YYYYMMDD
    var date = new Date(userDate),
        month = '' + (date.getMonth() + 1),
        day = '' + date.getDay(),
        year = date.getFullYear();
    
    if (month.length < 2) {
      month = '0' + month
    }
    if (day.length < 2) {
      day = '0' + day
    }
    
    return [year, month, day].join('')
  
  }
  
  console.log(formatDate("12/31/2014"));