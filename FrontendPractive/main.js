//  Debouncing
const debouncing = (fn, delay) =>{
    let timer;
    return function(){
        clearTimeout(timer)
        timer = setTimeout(()=>{
          fn.apply(this, arguments)
        }, delay)
    }
  }
  
  
  const callApi = ()=>{
    console.log("API")
  }
  const debounce = debouncing(callApi, 300)
  
  // Throttling
  const throttle = (fn, delay) =>{
    let flag = true
  return function(){
    // console.log(flag)
    if (flag){
      fn.apply(this, arguments)
      flag = false
      setTimeout(()=>{
        flag = true
      }, delay)
    }
  }
  }
  
  const throttling = throttle(callApi, 500)
  
  // # TicTacToe
  var modal = document.querySelector(".modal")
  var activeUserBool = true
  user1  = []
  user2 = []
  
  var chances = 0
  
  const winningConditions = []
  
  const condition = []
  
  for(let i=0; i<3 ; i++){
    condition.push(i)
  }
  
  const generateWinningCondition=(size)=>{
    for(let i = 0; i< size; i++){
      winningConditions.push(condition.map(row =>i*size + row))
      winningConditions.push(condition.map(row =>row*size + i))
    }
  
    winningConditions.push(condition.map(row=>row*size+row))
    winningConditions.push(condition.map(row=>(row+1)*size-(row+1)))
  }
  
  generateWinningCondition(3)
  
  
  const switchUser = ()=>{
    activeUserBool =  activeUserBool ? false : true
  }
  
  
  const gridContainer = document.querySelector(".tic-tac-toe");
  
      // Loop to create cells
  for (let i = 1; i <= 9; i++) {
    const cell = document.createElement("div");
    cell.classList.add("cell");
    cell.setAttribute("data-key", i);
    gridContainer.appendChild(cell);
  }
  
  const cellArray = document.querySelectorAll(".cell")
  
  cellArray.forEach((cell, index)=>{
    cell.addEventListener('click', ()=>{
        chances +=1
  
        if (activeUserBool){
          user1.push(index)
          cell.innerHTML = 'X'
        }else{
          user2.push(index)
          cell.innerHTML = '0'
        }
  
  
        if (checkValidation(activeUserBool?user1:user2)){
          showModal(activeUserBool ? "User 1 has Won" : "User 2 has Won")
        }
        activeUserBool = !activeUserBool
  
        if (chances == 9){
          console.log("draw")
          showModal("Games is a Draw")
        }
    })
  
  })
  
  const checkValidation = (userVal) =>{
    let won = false
    winningConditions.forEach((el,index)=>{
      let check = 0
      el.forEach((con,i)=>{
        if (userVal.indexOf(con) != -1){
          check+=1
          if (check == 3){
            won = true
          }
        }
      })
     })
  
     return won
  }
  
  const showModal = (content)=>{
    toggleModal()
    modal.innerHTML = content
  }
  
  const toggleModal = ()=>{
    modal.classList.toggle("showModal");
  }
  
  
  // Snake and Ladder
  // game.js
  
  // Game constants
  const boardSize = 10;
  const playerCount = 2;
  const snakes = { 16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78 };
  const ladders = { 1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100 };
  
  // Game state
  let players = Array(playerCount).fill(0); // Initialize player positions
  let currentPlayer = 0;
  
  // Create game board
  function createBoard() {
    const board = document.getElementById('board');
    board.innerHTML = ''; // Clear existing board
  
    // Create cells for the board
    for (let i = boardSize * boardSize; i > 0; i--) {
      const cell = document.createElement('div');
      cell.classList.add('cell');
      cell.innerText = i;
      board.appendChild(cell);
    }
  }
  
  // Roll dice
  function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
  }
  
  // Move player
  function movePlayer(player, steps) {
    let newPosition = players[player] + steps;
  
    // Check for snakes and ladders
    if (snakes[newPosition]) {
      newPosition = snakes[newPosition];
    } else if (ladders[newPosition]) {
      newPosition = ladders[newPosition];
    }
  
    // Update player position
    players[player] = newPosition <= boardSize * boardSize ? newPosition : players[player];
  
    // Update board display
    updateBoard();
  
    // Check for win condition
    if (players[player] === boardSize * boardSize) {
      document.getElementById('status').innerText = `Player ${player + 1} wins!`;
      document.getElementById('rollDiceBtn').disabled = true; // Disable dice rolling
    } else {
      // Switch to next player
      currentPlayer = (currentPlayer + 1) % playerCount;
      document.getElementById('status').innerText = `Player ${currentPlayer + 1}'s turn`;
    }
  }
  
  // Update board display
  function updateBoard() {
  
    const cells = document.querySelectorAll('.cell');
    cells.forEach(cell => {
      cell.innerHTML = cell.innerText; // Reset cell content
    });
  
    // Place players on the board
    players.forEach((position, index) => {
      console.log(position, "pos")
      console.log(cells[position])
      const playerDiv = document.createElement('div');
      playerDiv.classList.add('player');
      const cellIndex = boardSize * boardSize - position;
      if (cells[cellIndex]) {
        cells[cellIndex].appendChild(playerDiv);
      }
    });
  }
  
  // Initialize game
  function initGame() {
    createBoard();
  
    document.getElementById('rollDiceBtn').addEventListener('click', () => {
      const diceRoll = rollDice();
      document.getElementById('status').innerText = `Player ${currentPlayer + 1} rolled a ${diceRoll}`;
      movePlayer(currentPlayer, diceRoll);
    });
  
    updateBoard();
  }
  
  // Start the game
  initGame();
  
  
//   Infinite Scroll
  
//   document.addEventListener('DOMContentLoaded',()=>{
    let userContainer = document.getElementById("users__container")
    let page = 1
    let loading = false
  
    let addUser = (data) => {
      let user = `<div class="user">
              <div class="user-logo item">
                <img src="${data.picture.large}" alt="user" />
              </div>
              <div class="user-name item">${data.name.first} ${data.name.last}</div>
              <div class="user-country item">${data.location.country}</div>
              <div class="user-email item">${data.email}</div>
            </div>
    `
      userContainer.insertAdjacentHTML("beforeend", user)
    }
    let data = []
    
    const fetchData = async (pageNumber) => {
      console.log(pageNumber)
      try {
        let url = `https://randomuser.me/api/?page=${pageNumber}&results=${10}&seed=abc`;
        const res = await fetch(url)
        const data = await res.json()
        page+=1
        loading = false
        return data
      } catch (error) {
        
      }
    
    }
    window.addEventListener('scroll',(eve)=>{
      const { scrollTop, scrollHeight, clientHeight } = document.documentElement;
      if(scrollTop +clientHeight >= scrollHeight-5){
        renderData(page)
      }
    })
  
    const renderData = async (pageNumber)=>{
      if (loading) return;
      loading = true;
      document.querySelector(".loaderContainer").style.opacity = 1
      try {
        let users = await fetchData(pageNumber)
          users.results.forEach((el, index) => {
          addUser(el);
        });
        document.querySelector(".loaderContainer").style.opacity = 0
      } catch (error) {
        console.error('Error fetching or processing data:', error);
      }
    }
    
    (async function() {
      renderData(page)
    }())
  
  let toDo = document.querySelector(".toDo")
  let toDo_tasks = document.querySelector(".toDo_tasks")
  
  let progress = document.querySelector(".progress")
  let progress_tasks = document.querySelector(".progress_tasks")
  
  let completed = document.querySelector(".completed")
  let completed_tasks = document.querySelector(".completed_tasks")
  
  let modal = document.querySelector(".modalBackgroud")
  let taskInput = document.querySelector("#newTask")
  let taskColumn = document.querySelectorAll('.tasks')
  
  let addTask = document.querySelector(".addTask")
  let addNewTask = document.querySelector(".addNewTask")
  
  let cards = document.querySelectorAll(".card")
  
  
  let currentSection = ""
  let task = ""
  
  let trello = {
    toDo_tasks : [],
    progress_tasks : [],
    completed_tasks : []
  }
  
  let idGenerator = 1
  
  
  addTask.addEventListener('click', (e)=>{
    modal.classList.toggle("showModal");
    currentSection = e.target.dataset.section
  })
  
  addNewTask.addEventListener('click', (e)=>{
    modal.classList.toggle("showModal");
    task = taskInput.value;
    console.log(currentSection)
    trello[currentSection].push({id:idGenerator, task})
    idGenerator+=1
    renderAllTasks()
    currentSection = ""
    task = ""
  })
  
  const renderTask = (nameStr, taskName) =>{
    console.log(trello,"object", taskName, nameStr)
    taskName.innerHTML = ''
    trello[nameStr].forEach((el,index)=>{
      let car = document.createElement('div');
      car.className = 'card';
      car.draggable = true;
      car.dataset.section = nameStr
      car.dataset.task_id = el.id
  
      let taskText = document.createElement('span');
      taskText.textContent = el.task;
    
  
      let removeButton = document.createElement('button');
      removeButton.className = 'removeTask';
      removeButton.textContent = 'X';
      removeButton.dataset.task_id = el.id
  
      removeButton.onclick = () => {
        deleteTask(el.id, 'toDo');
      };
  
      car.appendChild(taskText);
      car.appendChild(removeButton);
      car.addEventListener('dragstart',(e)=>dragStart(e))
      car.addEventListener('dragEnd',(e)=>dragEnd(e))
      taskName.appendChild(car);
    })
  }
  
  const deleteTask = (id, section)=>{
    console.log(section, id)
    trello[section] = trello[section].filter(el => el.id !== id);
    
    renderTask()
  }
  
  
  const renderAllTasks = () => {
    renderTask('toDo_tasks',toDo_tasks);
    renderTask('progress_tasks', progress_tasks);
    renderTask('completed_tasks', completed_tasks);
  }
  
  
  
  
  
  
  const dragStart = (e)=>{
    console.log(e.target.dataset.task_id, e.target.dataset.section)
    e.dataTransfer.setData('task_id', e.target.dataset.task_id);
    e.dataTransfer.setData('section', e.target.dataset.section);
  }
  
  const dragEnd = ()=>{
    e.preventDefault();
  }
  
  
  const dragover = (e)=>{
    e.preventDefault();
    console.log('DragOver')
  }
  
  const dragenter = (e)=>{
    e.preventDefault();
  }
  
  const dragleave = (e)=>{
    e.preventDefault();
  }
  
  const drop = (e)=>{
    e.preventDefault();
    const id = e.dataTransfer.getData('task_id');
    const oldSection = e.dataTransfer.getData('section');
    const newSection = e.currentTarget.classList[1];
    console.log(id, oldSection, newSection)
    if (oldSection !== newSection) {
      // Find the task in the old section
      const taskIndex = trello[oldSection].findIndex(task => task.id == id);
      const task = trello[oldSection][taskIndex];
  
      // Remove from old section and add to new section
      trello[oldSection].splice(taskIndex, 1);
      trello[newSection].push(task);
  
      // Re-render all tasks
      renderAllTasks();
    }
  }
  
  
  taskColumn.forEach((col, index)=>{
    col.addEventListener('dragover', (e)=>dragover(e))
    col.addEventListener('dragenter', (e)=>dragenter(e))
    col.addEventListener('dragleave', (e)=>dragleave(e))
    col.addEventListener('drop', (e)=>drop(e))
  })
  