try:
    with open('missing_file.csv','r') as f:
        data=f.read()
except Exception as e:
    with open('MISSING_FILE.csv','r') as f:
        data=f.read()
    print('File not found : Pipeline cannot proceed.')
    print(f"Error: {e}")
    
finally:
    print('Execution completed.')
 