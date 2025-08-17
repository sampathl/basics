import { useEffect, useState } from 'react';
import TodoList from './Todolist';
import './App.css';

function App() {

  const [newItem, setNewItem] = useState("")
  const [data,setData] = useState("")
  const [todoList, setTodoList] = useState(()=>{
    const localValue = localStorage.getItem("TODO");
    if (localValue === null || localValue === "undefined") return [];
    try {
      return JSON.parse(localValue);
    } catch (e) {
      console.error("Error parsing local storage value", e);
      return [];
    }
    
  } );



  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
    .then(response => {
      if (!response.ok){return Error("network error")}
      return response.json()
    })
    .then(data => {setData(data)})
    .catch(error => console.log(error.message))
  }, []);


  useEffect(() => {
    localStorage.setItem("TODO", JSON.stringify(todoList));
  }, [todoList]);

  const handleOnChange = (e) => {
    console.log("on change");
    setNewItem(e.target.value)
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("this should be good")
    setTodoList((todoList) => {
      return [...todoList, newItem]
    })
    setNewItem("")
  }

  const handleDelete = (e) => {
    console.log(e.target.value)
    setTodoList((todoList) => {
      return todoList.filter((todo) => todo !== e.target.value)
    })
  }

  console.log(data)

  return (
    <div className="App">
      <>
        <h1>Todo Do List</h1>
        <form onSubmit={handleSubmit}>
          <input
            value={newItem}
            type="text"
            placeholder="Enter new todo"
            onChange={handleOnChange}
          />
          <button type="submit">{"add todo"} </button>
        </form>
      </>
      <TodoList todoList={todoList} handleDelete={handleDelete}/>


    </div>
  );
}

export default App;
