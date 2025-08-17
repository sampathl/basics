import { useState } from 'react';
import './App.css';

export default function TodoList({todoList,handleDelete}) {


  return (
    <div className="TodoList">
        <h1>{"TODO"}</h1>
        {todoList.map((todo, index) => {
          return <div key={index}>
            <label>
              <input key={index} type="checkbox" />
              {todo}
              <button onClick={handleDelete} value={todo}>{"Delete"}</button>
            </label>
          </div>
          

        })}
    </div>
  );
};

