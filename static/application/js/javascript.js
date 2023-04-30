const url = `/application`;

function my_function() {
    alert('Application - Page')
}

function get_applications() {
   let url = `/application/id`
   fetch(url, {headers: {'Accept': 'application/json'}}, {method: 'GET'})
      .then(response => response.json())
      .then(data => {
        console.log(data)

      })
}

function get_application(id) {
   let url = `/application/id`
   fetch(url, {headers: {'Accept': 'application/json'}}, {method: 'GET'})
      .then(response => response.json())
      .then(data => {
        console.log(data)
      })
}

function update_application() {
   let url = `/application/id`
   fetch(url, {headers: {'Accept': 'application/json'}}, {method: 'PATCH'})
      .then(response => response.json())
      .then(data => {
        console.log(data)

      })
}

function update_full_application() {
   let url = `/application/id`
   fetch(url, {headers: {'Accept': 'application/json'}}, {method: 'PUT'}, {body: {}})
      .then(response => response.json())
      .then(data => {
        console.log(data)
      })}

function delete_application() {
   let url = `/application/id`
   fetch(url, {headers: {'Accept': 'application/json'}}, {method: 'DELETE'})
      .then(response => response.json())
      .then(data => {
        console.log(data)
      })
}