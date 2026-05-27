"""Lightweight resource monitor for overlay display."""

import time
import psutil
import os


class ResourceMonitor:
    def __init__(self, sample_interval: float = 1.0):
        self._interval = sample_interval
        self._process = psutil.Process(os.getpid())
        self._last_sample = 0.0
        self._cpu_percent = 0.0
        self._mem_mb = 0.0
        self._sys_cpu = 0.0

    def update(self):
        now = time.time()
        if now - self._last_sample >= self._interval:
            self._cpu_percent = self._process.cpu_percent(interval=None)
            self._mem_mb = self._process.memory_info().rss / (1024 * 1024)
            self._sys_cpu = psutil.cpu_percent(interval=None)
            self._last_sample = now

    @property
    def cpu(self) -> float:
        return self._cpu_percent

    @property
    def mem_mb(self) -> float:
        return self._mem_mb

    @property
    def sys_cpu(self) -> float:
        return self._sys_cpu
