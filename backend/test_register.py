# backend/test_register.py

from blockchain import contract

file_id = "test_file_001"
file_hash = "abc123def456789"  # you can simulate any SHA256 hash here

tx = contract.register_file(file_id, file_hash)
print("✅ Transaction sent! Tx Hash:", tx)
