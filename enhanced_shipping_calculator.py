# Enhanced Shipping Cost Calculator
# Improved version with multiple shipping options, validation, and better UX

import re
from datetime import datetime, timedelta

class ShippingCalculator:
    def __init__(self):
        # Different shipping rates per kg based on service type
        self.shipping_rates = {
            'standard': 2.50,
            'express': 4.00,
            'overnight': 7.50
        }
        
        # Base costs for different service types
        self.base_costs = {
            'standard': 5.00,
            'express': 12.00,
            'overnight': 25.00
        }
        
        # Delivery timeframes (in business days)
        self.delivery_times = {
            'standard': 5,
            'express': 2,
            'overnight': 1
        }
    
    def validate_weight(self, weight):
        """Validate package weight input"""
        if weight <= 0:
            raise ValueError("Package weight must be greater than 0")
        if weight > 50:
            raise ValueError("Package weight cannot exceed 50kg")
        return True
    
    def validate_zip_code(self, zip_code):
        """Validate US ZIP code format"""
        zip_pattern = r'^\d{5}(-\d{4})?$'
        if not re.match(zip_pattern, zip_code):
            raise ValueError("Invalid ZIP code format. Use 12345 or 12345-6789")
        return True
    
    def calculate_distance_multiplier(self, origin_zip, dest_zip):
        """Calculate distance multiplier based on ZIP codes"""
        origin_num = int(origin_zip[:5])
        dest_num = int(dest_zip[:5])
        zip_diff = abs(origin_num - dest_num)
        
        if zip_diff < 10000:
            return 1.0  # Local delivery
        elif zip_diff < 30000:
            return 1.3  # Regional delivery
        elif zip_diff < 50000:
            return 1.6  # National delivery
        else:
            return 2.0  # Cross-country delivery
    
    def calculate_shipping_cost(self, weight, service_type, origin_zip=None, dest_zip=None):
        """Calculate total shipping cost"""
        # Validate inputs
        self.validate_weight(weight)
        
        if service_type not in self.shipping_rates:
            raise ValueError(f"Invalid service type. Choose from: {list(self.shipping_rates.keys())}")
        
        # Base calculation
        base_cost = self.base_costs[service_type]
        weight_cost = weight * self.shipping_rates[service_type]
        subtotal = base_cost + weight_cost
        
        # Apply distance multiplier if ZIP codes provided
        distance_multiplier = 1.0
        if origin_zip and dest_zip:
            self.validate_zip_code(origin_zip)
            self.validate_zip_code(dest_zip)
            distance_multiplier = self.calculate_distance_multiplier(origin_zip, dest_zip)
        
        total_cost = subtotal * distance_multiplier
        
        # Apply volume discount for heavy packages
        if weight > 20:
            total_cost *= 0.9  # 10% discount
            discount_applied = True
        else:
            discount_applied = False
        
        return {
            'base_cost': base_cost,
            'weight_cost': weight_cost,
            'subtotal': subtotal,
            'distance_multiplier': distance_multiplier,
            'total_cost': total_cost,
            'service_type': service_type,
            'delivery_days': self.delivery_times[service_type],
            'discount_applied': discount_applied
        }
    
    def get_delivery_date(self, service_type):
        """Calculate estimated delivery date"""
        days = self.delivery_times[service_type]
        delivery_date = datetime.now() + timedelta(days=days)
        # Skip weekends for business days calculation
        while delivery_date.weekday() >= 5:  # Saturday = 5, Sunday = 6
            delivery_date += timedelta(days=1)
        return delivery_date.strftime("%Y-%m-%d")
    
    def display_quote(self, result):
        """Display formatted shipping quote"""
        print("\n" + "="*50)
        print("           SHIPPING QUOTE")
        print("="*50)
        print(f"Service Type: {result['service_type'].title()}")
        print(f"Base Cost: ${result['base_cost']:.2f}")
        print(f"Weight Cost: ${result['weight_cost']:.2f}")
        print(f"Distance Multiplier: {result['distance_multiplier']:.1f}x")
        
        if result['discount_applied']:
            print(f"Volume Discount: 10% (Weight > 20kg)")
        
        print("-" * 30)
        print(f"TOTAL COST: ${result['total_cost']:.2f}")
        print(f"Estimated Delivery: {result['delivery_days']} business days")
        print(f"Expected Delivery Date: {self.get_delivery_date(result['service_type'])}")
        print("="*50)

def main():
    """Interactive shipping calculator"""
    calculator = ShippingCalculator()
    
    print("🚚 Enhanced Shipping Cost Calculator")
    print("Available services: standard, express, overnight")
    print("-" * 50)
    
    try:
        # Get package weight
        weight = float(input("Enter package weight (kg): "))
        
        # Get service type
        print("\nAvailable shipping services:")
        for service, rate in calculator.shipping_rates.items():
            print(f"  {service}: ${rate}/kg + base cost")
        
        service_type = input("Select service type [standard]: ").strip().lower()
        if not service_type:
            service_type = 'standard'
        
        # Get ZIP codes (optional)
        use_zip = input("Include ZIP codes for distance calculation? (y/n) [n]: ").strip().lower()
        origin_zip = None
        dest_zip = None
        
        if use_zip == 'y':
            origin_zip = input("Enter origin ZIP code: ").strip()
            dest_zip = input("Enter destination ZIP code: ").strip()
        
        # Calculate and display result
        result = calculator.calculate_shipping_cost(
            weight, service_type, origin_zip, dest_zip
        )
        calculator.display_quote(result)
        
        # Offer comparison
        compare = input("\nShow comparison with other services? (y/n) [n]: ").strip().lower()
        if compare == 'y':
            print("\n" + "="*60)
            print("                SERVICE COMPARISON")
            print("="*60)
            
            for service in calculator.shipping_rates.keys():
                if service != service_type:
                    comp_result = calculator.calculate_shipping_cost(
                        weight, service, origin_zip, dest_zip
                    )
                    print(f"{service.title()}: ${comp_result['total_cost']:.2f} "
                          f"({comp_result['delivery_days']} days)")
    
    except ValueError as e:
        print(f"❌ Error: {e}")
    except KeyboardInterrupt:
        print("\n\n👋 Calculator session ended.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()