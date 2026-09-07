from enum import Enum


class InvoicesListPaymentGateway(str, Enum):
    @classmethod
    def _missing_(cls, value: object):
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = f"UNKNOWN_{value}"
        member._value_ = value
        return member

    ANYMONEY = "anymoney"
    BINANCE = "binance"
    BRAINTREE = "braintree"
    BTCPAY = "btcpay"
    CHECKOUTCOM = "checkoutcom"
    COINBASE = "coinbase"
    COINGATE = "coingate"
    COINPAYMENTS = "coinpayments"
    COMGATE = "comgate"
    CRYPTOMUS = "cryptomus"
    GOPAY = "gopay"
    HALYK_EPAY = "halyk_epay"
    IYZICO = "iyzico"
    KASPI_PAY = "kaspi_pay"
    LIQPAY = "liqpay"
    MANUAL = "manual"
    MOLLIE = "mollie"
    MONEI = "monei"
    MONOBANK = "monobank"
    NEXI_XPAY = "nexi_xpay"
    NOWPAYMENTS = "nowpayments"
    PAYONE = "payone"
    PAYPLUG = "payplug"
    PAYTR = "paytr"
    PAYTRAIL = "paytrail"
    PAYU = "payu"
    PRZELEWY24 = "przelewy24"
    REDSYS = "redsys"
    STRIPE = "stripe"
    TPAY = "tpay"
    UNZER = "unzer"
    USEGATEWAY = "usegateway"
    VIPPS_MOBILEPAY = "vipps_mobilepay"
    WALLET = "wallet"
    WAYFORPAY = "wayforpay"
    WHITEPAY = "whitepay"

    def __str__(self) -> str:
        return str(self.value)
