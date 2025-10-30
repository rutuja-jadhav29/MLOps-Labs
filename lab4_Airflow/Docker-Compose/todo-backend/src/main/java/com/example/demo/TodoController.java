package com.example.demo;

import org.springframework.web.bind.annotation.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;

@RestController
@RequestMapping("/tasks")
@CrossOrigin(origins = "*") // allow requests from frontend (port 5000)
public class TodoController {

    private final List<Map<String, Object>> tasks = new ArrayList<>();
    private final AtomicInteger idCounter = new AtomicInteger();

    @GetMapping
    public Map<String, Object> getTasks() {
        return Map.of("tasks", tasks);
    }

    @PostMapping
    public void addTask(@RequestBody Map<String, String> body) {
        String task = body.get("task");
        if (task != null && !task.isEmpty()) {
            int id = idCounter.incrementAndGet();
            tasks.add(Map.of("id", id, "task", task));
        }
    }

    @DeleteMapping("/{id}")
    public void deleteTask(@PathVariable int id) {
        tasks.removeIf(t -> (int) t.get("id") == id);
    }
}
