// Task 1. =============================================================================
let myHeader = document.createElement('header');
let position = document.getElementsByTagName('body')[0].children[0];
document.getElementsByTagName('body')[0].insertBefore(myHeader, position);

let divButtons = document.createElement('div');
divButtons.className = 'buttons';
divButtons.style.textAlign = 'center';
divButtons.style.background = '#ECEBBD';
divButtons.style.borderRadius = '10px';
divButtons.style.marginBottom = '5px';

const buttonOptions = ['Додати в друзі', 'Написати повідомлення', 'Запропонувати роботу'];
buttonOptions.map(buttonName => {
    let button = document.createElement('button');
    button.innerText = buttonName;
    button.style.fontSize = '15px';
    button.style.margin = '10px';
    button.style.background = '#d2d2ce';
    divButtons.appendChild(button);
})
document.getElementsByTagName('header')[0].appendChild(divButtons);


// Task 2. =============================================================================
function getRandomInt() {
    let min = Math.ceil(10);
    let max = Math.floor(1000);
    return Math.floor(Math.random() * (max - min + 1) + min);
}

let randomAmount = getRandomInt();

let friendsAmount = document.createElement('button');
friendsAmount.id = 'btn-amount';
friendsAmount.innerText = `Кількість друзів: ${randomAmount}`;
friendsAmount.style.fontSize = '15px';
friendsAmount.style.margin = '5px';
friendsAmount.style.background = '#77de62';
divButtons.appendChild(friendsAmount);

document.getElementsByTagName('header')[0].appendChild(divButtons);

const buttonAddFriend = document.getElementsByTagName('button')[0];
const buttonFriendAmount = document.getElementById('btn-amount');
buttonAddFriend.onclick = (event) => {
    buttonFriendAmount.innerText = `Кількість друзів: ${++randomAmount}`;}


// Task 3. ============================
buttonAddFriend.addEventListener('click', (event) => {
    event.target.innerText = 'Очікується підтвердження';
    event.target.disabled = true;
})

// Task 4. =============================================================================
let clickCounter = 0;
const colors = ['#d2d2ce', '#e72e5a'];
const buttonWriteMessage = document.getElementsByTagName("button")[1];
buttonWriteMessage.onclick = (event) => {
    ++clickCounter;
    event.target.style.background = colors[clickCounter % 2];
}


// Task 5. =============================================================================
const hiddenOptions = [true, false]
let jobCounter = 0;
const buttonOfferJob = document.getElementsByTagName('button')[2];
buttonOfferJob.onclick = (event) => {
    buttonAddFriend.hidden = hiddenOptions[jobCounter % 2];
    ++jobCounter;
}


// Task 6. =============================================================================
const buttonHW = document.createElement('button');
buttonHW.style.position = 'center';
buttonHW.innerText = 'Здати ДЗ';
buttonHW.style.background = 'rgba(225,234,229,0.85)';
buttonHW.style.marginTop = '10px';
buttonHW.style.fontSize = '15px';
buttonHW.style.padding = '10px';
buttonHW.style.width = '100%';
buttonHW.style.borderRadius = '10px';

document.getElementsByTagName('div')[2].appendChild(buttonHW);

buttonHW.onclick = (event) => {
    const tableRaw  = document.createElement('tr');

    let tdLeft = document.createElement('td');
    tdLeft.className = 'tleft';
    tdLeft.innerText = '№27 «Базовий JS»';
    tableRaw.appendChild(tdLeft);

    let tdRight = document.createElement('td');
    tdRight.className = 'tright';
    tdRight.innerText = '5 / 5';
    tableRaw.appendChild(tdRight);

    document.getElementsByTagName('tbody')[0].appendChild(tableRaw);
}
