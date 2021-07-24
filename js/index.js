function postData(url, data) {
    // Default options are marked with *
    return fetch(url, {
        body: JSON.stringify(data), // must match 'Content-Type' header
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, same-origin, *omit
        headers: {
            'user-agent': 'Example',
            'content-type': 'application/json'
        },
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, cors, *same-origin
        redirect: 'follow', // manual, *follow, error
        referrer: 'no-referrer', // *client, no-referrer
    })
        .then(response => response.json()) // 輸出成 json
}

function submit_cost(){
    const uid_cost = document.getElementById('uid_cost').value;

    const data = {
        'uid_cost': uid_cost
    }
    document.getElementById('cost_output').innerHTML=
    'Usage Account ID：' + uid_cost

    postData('http://192.168.39.158:3000/cost', data)
    .then(data=>{
        console.log(JSON.stringify(data, null, '\t'));

        var mycost = JSON.stringify(data, null, '\t');
        document.getElementById('resultcost').innerHTML=
        '<pre>' + mycost + '</pre>';
    })

}

function submit_amount(){
    const uid_amount = document.getElementById('uid_amount').value;

    const data = {
        'uid_amount': uid_amount
    }
    document.getElementById('amount_output').innerHTML=
    'Usage Account ID：' + uid_amount

    postData('http://192.168.39.158:3000/amount', data)
    .then(data=>{
        console.log(JSON.stringify(data, null, '\t'));

        var myamount = JSON.stringify(data, null, '\t');
        document.getElementById('resultamount').innerHTML=
        '<pre>' + myamount + '</pre>';
    })

}

function list_uid(){
    
    const pid_uid = document.getElementById('pid_uid').value;

    const data = {
        'pid_uid': pid_uid
    }
    document.getElementById('payerid').innerHTML=
    'Payer Account ID：' + pid_uid

    postData('http://192.168.39.158:3000/uid', data)
    .then(data=>{
        console.log(JSON.stringify(data, null, '\t'));

        var myuid = JSON.stringify(data, null, '\t');
        document.getElementById('resultid').innerHTML=
        '<pre>' + myuid + '</pre>';
    })

}

function submit_count(){
    const uid_count = document.getElementById('uid_count').value;

    const data = {
        'uid_count': uid_count
    }
    document.getElementById('count_output').innerHTML=
    'Usage Account ID：' + uid_count

    postData('http://192.168.39.158:3000/count', data)
    .then(data=>{
        console.log(JSON.stringify(data, null, '\t'));

        var mycount = JSON.stringify(data, null, '\t');
        document.getElementById('resultcount').innerHTML=
        '<pre>' + mycount + '</pre>';
    })

}