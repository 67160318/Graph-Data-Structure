from cpu import CPU
from ram import RAM
from storage import Storage
from computer import Computer

print("=== การสร้างและทดสอบคอมพิวเตอร์ ===")
cpu_specs = {"brand": "Intel", "model": "Core i7-13700K", "cores": 8, "base_speed": 3.4}
ram_specs = {"brand": "Corsair", "capacity": 32, "speed": 3200}
storage_specs = {"storage_type": "SSD", "brand": "Samsung", "capacity": 1000, "read_speed": 550, "write_speed": 520}
my_computer = Computer(brand="ASUS", model="ROG Strix", cpu_specs=cpu_specs, ram_specs=ram_specs, storage_specs=storage_specs)

print(my_computer.power_on())
print("=== สถานะระบบ ===")
print(my_computer.get_system_status())
print(my_computer.power_off())

print("\n=== การติดตั้งโปรแกรม ===")
print(my_computer.power_on())
print(my_computer.install_program("Microsoft Office", 3.5, 1.2))
print(my_computer.install_program("Adobe Photoshop", 2.8, 2.5))
print(my_computer.install_program("Google Chrome", 0.5, 0.8))

print("\n=== การรันโปรแกรม ===")
print(my_computer.run_program("Microsoft Office", 3))
print(my_computer.run_program("Adobe Photoshop", 7))
print(my_computer.run_program("Google Chrome", 2))

print("\n=== การใช้งานหนักและการจัดการระบบ ===")
print(my_computer.run_program("Adobe Photoshop", 9))
print(my_computer.run_program("Adobe Photoshop", 9))
print(my_computer.install_program("Game XYZ", 50, 8))

print("\n=== สถานะระบบหลังใช้งานหนัก ===")
print(my_computer.get_system_status())

print("\n=== การตรวจสอบประสิทธิภาพ ===")
print(my_computer.check_performance())

print(my_computer.cpu.cool_down())

print("\n=== สถานะระบบหลังระบายความร้อน ===")
print(my_computer.get_system_status())